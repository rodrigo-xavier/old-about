from . import forms
from . import models
from django.shortcuts import (render, get_object_or_404)
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from django.db.models import Count
import reversion
from django.db import transaction


def profile(request):
    profile = models.Profile.objects.first()
    education = models.Education.objects.all()
    xp = models.XP.objects.all()
    current_xp = models.XP.objects.filter(is_current=True)
    current_education = models.Education.objects.filter(is_current=True)
    data = {
        'profile':profile, 
        'xp':xp, 
        'education':education,
        'current_xp':current_xp,
        'current_education':current_education,
    }
    return render(request, 'cv/profile.html', data)

@login_required(login_url='/root/')
@transaction.atomic
@reversion.views.create_revision(manage_manually=False, using=None, atomic=True, request_creates_revision=None)
def edit_profile(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    LanguageFormSet = inlineformset_factory(
        parent_model=models.Profile,
        model=models.Language,
        form=forms.LanguageForm,
        exclude=('profile',),
        extra=1,
    )

    if request.method == "GET":
        user = forms.UserForm(instance=request.user)
        profile = forms.ProfileForm(instance=request.user.profile)
        language = LanguageFormSet(instance=request.user.profile)

    else: #POST
        user = forms.UserForm(request.POST, instance=request.user)
        profile = forms.ProfileForm(request.POST, instance=request.user.profile)
        language = LanguageFormSet(request.POST, instance=request.user.profile)
        if user.is_valid() and profile.is_valid() and language.is_valid():
            user.save()
            profile.save()
            language.save()
            return redirect("cv:Edit Profile")
    
    data = {
        'user': user,
        'profile': profile,
        'languages': language,
    }

    return render(request, 'cv/edit_profile.html', data)


@login_required(login_url='/root/')
@reversion.views.create_revision(manage_manually=False, using=None, atomic=True, request_creates_revision=None)
def edit_xp(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    profile = models.Profile.objects.first()

    XPFormSet = inlineformset_factory(
        parent_model=models.Profile,
        model=models.XP,
        form=forms.XPForm,
        exclude=('profile',),
        extra= 1 + int(request.GET.get('new')) if request.GET.get('new') else 1, # Pega o valor extra do formulario e adiciona +1 quando o botao 'new' eh pressionado, criando outro formulario
        max_num=15,
        can_delete=True
    )
    extra = XPFormSet.extra
    
    if request.method == "GET":
        if hasattr(profile, "xp_set") and (profile.xp_set.count() != 0):
            xp = XPFormSet(instance=request.user)
        elif (profile is None):
            return redirect("cv:Edit Profile")
        else:
            xp = XPFormSet()

    else: #POST
        xp = XPFormSet(request.POST, instance=request.user)
        if xp.is_valid():
            xp.save()
            return redirect("cv:Edit XP")
    
    data = {
        'xp': xp, 
        'extra': extra,
        'profile': profile,
    }

    return render(request, 'cv/edit_xp.html', data)


@login_required(login_url='/root/')
@reversion.views.create_revision(manage_manually=False, using=None, atomic=True, request_creates_revision=None)
def edit_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    profile = models.Profile.objects.first()
    
    EducationFormSet = inlineformset_factory(
        parent_model=models.Profile,
        model=models.Education,
        form=forms.EducationForm, 
        exclude=('profile',),
        extra= 1 + int(request.GET.get('new')) if request.GET.get('new') else 1,
        max_num=15,
    )
    extra = EducationFormSet.extra

    if request.method == "GET":
        if hasattr(profile, "education_set") and (profile.education_set.count() != 0):
            education = EducationFormSet(instance=request.user)
        elif (profile is None):
            return redirect("cv:Edit Profile")
        else:
            education = EducationFormSet()
    
    else: #POST
        education = EducationFormSet(request.POST, instance=request.user)
        if education.is_valid():
            education.save()
            return redirect("cv:Edit Education")
    
    data = {
        'education': education, 
        'extra': extra,
        'profile': profile,
    }

    return render(request, 'cv/edit_education.html', data)

def schedule(request):
    profile = models.Profile.objects.first()

    data = {
        'profile': profile,
    }

    return render(request, 'schedule/schedule.html', data)
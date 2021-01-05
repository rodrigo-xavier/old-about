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

    user = User.objects.all().select_related('profile').get(username=request.user)

    LanguageFormSet = inlineformset_factory(
        parent_model=models.Profile,
        model=models.Language,
        form=forms.LanguageForm,
        exclude=('profile',),
        extra=1,
    )

    if request.method == "GET":
        user_form = forms.UserForm(instance=request.user)
        profile_form = forms.ProfileForm(instance=request.user.profile)
        language_form = LanguageFormSet(instance=request.user.profile)

    else: #POST
        user_form = forms.UserForm(request.POST, instance=request.user)
        profile_form = forms.ProfileForm(request.POST, instance=request.user.profile)
        language_form = LanguageFormSet(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid() and language_form.is_valid():
            user_form.save()
            profile_form.save()
            language_form.save()
            return redirect("cv:Edit Profile")
    
    data = {
        'user': user,
        'profile': user.profile,
        'user_form': user_form,
        'profile_form': profile_form,
        'languages_form': language_form,
    }

    return render(request, 'cv/edit_profile.html', data)


@login_required(login_url='/root/')
@reversion.views.create_revision(manage_manually=False, using=None, atomic=True, request_creates_revision=None)
def edit_xp(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    user = User.objects.all().select_related('profile').get(username=request.user)

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
        xp_form = XPFormSet(instance=request.user.profile)

    else: #POST
        xp_form = XPFormSet(request.POST, instance=request.user.profile)
        if xp_form.is_valid():
            xp_form.save()
            return redirect("cv:Edit XP")
    
    data = {
        'user': user,
        'profile': user.profile,
        'xp_form': xp_form, 
        'extra': extra,
    }

    return render(request, 'cv/edit_xp.html', data)


@login_required(login_url='/root/')
@reversion.views.create_revision(manage_manually=False, using=None, atomic=True, request_creates_revision=None)
def edit_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    user = User.objects.all().select_related('profile').get(username=request.user)
    
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
        education_form = EducationFormSet(instance=request.user.profile)
    
    else: #POST
        education_form = EducationFormSet(request.POST, instance=request.user.profile)
        if education_form.is_valid():
            education_form.save()
            return redirect("cv:Edit Education")
    
    data = {
        'user': user,
        'profile': user.profile,
        'education_form': education_form, 
        'extra': extra,
    }

    return render(request, 'cv/edit_education.html', data)

def schedule(request):
    user = User.objects.all().select_related('profile').get(username=request.user)

    data = {
        'profile': user.profile,
    }

    return render(request, 'schedule/schedule.html', data)
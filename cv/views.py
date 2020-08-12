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
@reversion.views.create_revision(manage_manually=False, using=None, atomic=True, request_creates_revision=None)
def edit_profile(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    profile = models.Profile.objects.first()

    if request.method == "GET":
        if not (profile is None):
            _profile = forms.ProfileForm(instance=profile)
        else:
            _profile = forms.ProfileForm()

    elif request.method == "POST":
        _profile = forms.ProfileForm(request.POST, instance=profile)
        if _profile.is_valid():
            try:
                _profile = _profile.save(commit=False)
                _profile.save()
                return redirect("cv:Edit Profile")

            except Exception as e:
                print(e)
    
    data = {
        'profile': profile,
        'profile_form': _profile,
    }

    return render(request, 'cv/edit_profile.html', data)


@login_required(login_url='/root/')
@reversion.views.create_revision(manage_manually=False, using=None, atomic=True, request_creates_revision=None)
def edit_xp(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    profile = models.Profile.objects.first()

    xp_inlineformset = inlineformset_factory(
        parent_model=models.Profile,
        model=models.XP,
        form=forms.XPForm,
        exclude=('profile',),
        extra= 1 + int(request.GET.get('new')) if request.GET.get('new') else 0,
        max_num=15,
        can_delete=True
    )
    extra = xp_inlineformset.extra
    
    if request.method == "GET":
        if hasattr(profile, "xp_set") and (profile.xp_set.count() != 0):
            xp = xp_inlineformset(instance=profile)
        elif (profile is None):
            return redirect("cv:Edit Profile")
        else:
            xp = xp_inlineformset()
    elif request.method == "POST":
        xp = xp_inlineformset(request.POST, instance=profile)
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
    
    education_inlineformset = inlineformset_factory(
        parent_model=models.Profile,
        model=models.Education,
        form=forms.EducationForm, 
        exclude=('profile',),
        extra= 1 + int(request.GET.get('new')) if request.GET.get('new') else 0,
        max_num=15,
    )
    extra = education_inlineformset.extra

    if request.method == "GET":
        if hasattr(profile, "education_set") and (profile.education_set.count() != 0):
            education = education_inlineformset(instance=profile)
        elif (profile is None):
            return redirect("cv:Edit Profile")
        else:
            education = education_inlineformset()
    elif request.method == "POST":
        education = education_inlineformset(request.POST, instance=profile)
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
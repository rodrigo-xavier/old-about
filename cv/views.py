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
    # academic = models.Academic.objects.all()
    # xp = models.XP.objects.all()
    # certification = models.Certification.objects.all()
    return render(request, 'cv/profile.html', {'profile':profile})

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

    return render(request, 'cv/edit_profile.html', {'profile': _profile})


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
    )
    extra = xp_inlineformset.extra
    
    if request.method == "GET":
        if (profile.xp_set.count() != 0):
            _xp = xp_inlineformset(instance=profile)
        elif (profile is None):
            return redirect("cv:Edit Profile")
        else:
            _xp = xp_inlineformset()
    elif request.method == "POST":
        _xp = xp_inlineformset(request.POST, instance=profile)
        if _xp.is_valid():
            _xp.save()
            return redirect("cv:Edit XP")

    return render(request, 'cv/edit_xp.html', {'xp': _xp, 'extra': extra})


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
        if (profile.education_set.count() != 0):
            _education = education_inlineformset(instance=profile)
        elif (profile is None):
            return redirect("cv:Edit Profile")
        else:
            _education = education_inlineformset()
    elif request.method == "POST":
        _education = education_inlineformset(request.POST, instance=profile)
        if _education.is_valid():
            _education.save()
            return redirect("cv:Edit Education")

    return render(request, 'cv/edit_education.html', {'education': _education, 'extra': extra})


@login_required(login_url='/root/')
@reversion.views.create_revision(manage_manually=False, using=None, atomic=True, request_creates_revision=None)
def edit_additional_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    profile = models.Profile.objects.first()

    # Conta objetos additionaleducation que tenham relacao com a instancia profile, utilizando aggregate, apenas para exibir conhecimentos
    # models.AdditionalEducation.objects.filter(profile=profile).aggregate(Count('profile'))['profile__count']
    
    additional_education_inlineformset = inlineformset_factory(
        parent_model=models.Profile,
        model=models.AdditionalEducation,
        form=forms.AdditionalEducationForm, 
        exclude=('profile', 'from_period', 'until_period'),
        extra= 1 + int(request.GET.get('new')) if request.GET.get('new') else 0,
        max_num=15,
    )
    extra = additional_education_inlineformset.extra
    
    if request.method == "GET":
        if (profile.education_set.count() != 0):
            _additional_education = additional_education_inlineformset(instance=profile)
        elif (profile is None):
            return redirect("cv:Edit Profile")
        else:
            _additional_education = additional_education_inlineformset()
    elif request.method == "POST":
        _additional_education = additional_education_inlineformset(request.POST, instance=profile)
        if _additional_education.is_valid():
            _additional_education.save()
            return redirect("cv:Edit Additional Education")

    return render(request, 'cv/edit_additional_education.html', {'additional_education': _additional_education, 'extra': extra})





def schedule(request):
    return render(request, 'schedule/schedule.html', {})
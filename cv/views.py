from . import forms
from . import models
from django.shortcuts import (render, get_object_or_404)
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory, modelformset_factory, inlineformset_factory


def profile(request):
    profile = models.Profile.objects.first()
    # academic = models.Academic.objects.all()
    # xp = models.XP.objects.all()
    # certification = models.Certification.objects.all()
    return render(request, 'cv/profile.html', {'profile':profile})



@login_required(login_url='/root/')
def edit(request, **kwargs):
    if not request.user.is_superuser:
        raise PermissionDenied

    return render(request, 'cv/edit.html', {})



@login_required(login_url='/root/')
def edit_profile(request, **kwargs):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = {}

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
                return redirect("cv:Edit")

            except Exception as e:
                print(e)
    
    form['profile'] = _profile

    return render(request, 'cv/edit_profile.html', {'form': form})


@login_required(login_url='/root/')
def edit_xp(request, **kwargs):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = {}

    xp = inlineformset_factory(
        parent_model=models.Profile,
        model=models.XP,
        form=forms.XPForm,
        exclude=('profile',),
        extra=1,
        max_num=15,
    )
    
    if request.method == "GET":
        _xp = xp()
    else:
        _xp = forms.XPForm(request.POST, instance=xp)
        if _xp.is_valid():
            try:
                _xp = _xp.save(commit=False)
                _xp.save()
                return redirect("cv:Edit")

            except Exception as e:
                print(e)

    return render(request, 'cv/edit_xp.html', {'form': form})


@login_required(login_url='/root/')
def edit_education(request, **kwargs):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = {}
    
    education = inlineformset_factory(
        parent_model=models.Profile,
        model=models.Education,
        form=forms.EducationForm, 
        exclude=('profile',),
        extra=1,
        max_num=15,
    )

    if request.method == "GET":
        _education = education()
    else:
        _education = forms.EducationForm(request.POST, instance=education)
        if _education.is_valid():
            try:
                _education = _education.save(commit=False)
                _education.save()
                return redirect("cv:Edit")

            except Exception as e:
                print(e)

    return render(request, 'cv/edit_education.html', {'form': form})


@login_required(login_url='/root/')
def edit_additional_education(request, **kwargs):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = {}
    
    additional_education = inlineformset_factory(
        parent_model=models.Profile,
        model=models.AdditionalEducation,
        form=forms.AdditionalEducationForm, 
        exclude=('profile',),
        extra=1,
        max_num=15,
    )

    if request.method == "GET":
        _additional_education = additional_education()
    else:
        _additional_education = forms.AdditionalEducationForm(request.POST, instance=additional_education)
        if _additional_education.is_valid():
            try:
                _additional_education = _additional_education.save(commit=False)
                _additional_education.save()
                return redirect("cv:Edit")

            except Exception as e:
                print(e)

    return render(request, 'cv/edit_additional_education.html', {'form': form})





def schedule(request):
    return render(request, 'schedule/schedule.html', {})
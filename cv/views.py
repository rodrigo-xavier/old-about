from . import forms
from . import models
from django.shortcuts import (render, get_object_or_404)
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def profile(request):
    profile = models.Profile.objects.first()
    # academic = models.Academic.objects.all()
    # xp = models.XP.objects.all()
    # certification = models.Certification.objects.all()
    return render(request, 'cv/profile.html', {'profile':profile})



@login_required(login_url='/root/')
def edit_profile(request, **kwargs):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = {}

    profile = models.Profile.objects.first()
    xp = models.XP.objects.first().profile.xp_set.all()
    # education = models.Education.objects.all()
    # additional_education = models.AdditionalEducation.objects.all()

    if request.method == "GET":
        if not (profile is None):
            profileform = forms.ProfileForm(instance=profile)
        else:
            profileform = forms.ProfileForm()

    elif request.method == "POST":
        profileform = forms.ProfileForm(request.POST, instance=profile)
        if profileform.is_valid():
            try:
                profileform = profileform.save(commit=False)
                profileform.save()
                return redirect("cv:Profile")

            except Exception as e:
                print(e)
    
    form['profile'] = profileform
    form['xp'] = xp
    # form['education'] = education
    # form['additional_education'] = profileform

    return render(request, 'cv/form_profile.html', {'form': form})


@login_required(login_url='/root/')
def edit_xp(request, **kwargs):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = {}

    xp = models.XP()
    

    if request.method == "GET":
        if not (xp is None):
            xpform = forms.XPForm(instance=xp)
        else:
            xpform = forms.XPForm()

    elif request.method == "POST":
        xpform = forms.XPForm(request.POST, instance=xp)
        if xpform.is_valid():
            try:
                xpform = xpform.save(commit=False)
                xpform.save()
                return redirect("cv:Profile")

            except Exception as e:
                print(e)
    
    form['xp'] = xpform

    return render(request, 'cv/form_profile.html', {'xp': xpform})


# @login_required(login_url='/root/')
# def edit_xp(request, **kwargs):
#     if not request.user.is_superuser:
#         raise PermissionDenied

#     profile = models.Profile.objects.first()
#     xp = models.XP.objects.all()
#     education = models.Education.objects.all()
#     additional_education = models.AdditionalEducation.objects.all()


#     if request.method == "GET":
#         if not (profile is None):
#             profileform = forms.ProfileForm(instance=profile)
#             # xpform = forms.ProfileForm(instance=xp)
#             # educationform = forms.ProfileForm(instance=education)
#             # additional_education_form = forms.ProfileForm(instance=additional_education)
#         else:
#             profileform = forms.ProfileForm()
#             xpform = forms.XPForm()
#             educationform = forms.EducationForm()
#             additional_education_form = forms.AdditionalEducationForm()

#     elif request.method == "POST":
#         if request.POST.get("save"):
#             profileform = forms.ProfileForm(request.POST, instance=profile)
#             if profileform.is_valid():
#                 try:
#                     profileform = profileform.save(commit=False)
#                     profileform.save()
#                     return redirect("cv:Profile")

#                 except Exception as e:
#                     print(e)
        
#         elif request.POST.get('xp'):
#             profileform = forms.ProfileForm(instance=profile)
#             print("deu certo porra")

#     return render(request, 'cv/form_profile.html', {'profile': profileform})



def schedule(request):
    return render(request, 'schedule/schedule.html', {})
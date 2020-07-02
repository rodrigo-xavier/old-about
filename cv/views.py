from . import forms
from . import models
from django.shortcuts import (render, get_object_or_404)
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def profile(request):
    profile = models.Profile.objects.first()
    return render(request, 'cv/profile.html', {'profile':profile})



@login_required(login_url='/root/')
def edit(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    profile = models.Profile.objects.first()

    if request.method == "GET":
        if not (profile is None):
            form = forms.ProfileForm(instance=profile)
        else:
            form = forms.ProfileForm()
    elif request.method == "POST":
        form = forms.ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            try:
                profileform = form.save(commit=False)
                profileform.last = datetime.now()
                profileform.save()
                return redirect("cv:Profile")

            except Exception as e:
                print(e)            

    return render(request, 'cv/form_profile.html', {'form': form})

def schedule(request):
    return render(request, 'schedule/schedule.html', {})
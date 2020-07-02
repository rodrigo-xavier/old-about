from . import forms
from . import models
from django.shortcuts import (render, get_object_or_404)
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.shortcuts import redirect


def profile(request):
    # profile = models.Profile.objects.all()
    return render(request, 'cv/profile.html', {})

def edit(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    if request.method == "GET":
        profile = models.Profile.objects.first()

        if not (profile is None):
            form = forms.ProfileForm.objects.first()
        else:
            form = forms.ProfileForm()
    elif request.method == "POST":
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            try:
                profileform = form.save(commit=False)
                profileform.last = timezone.now()
                profileform.save()
                return redirect("cv:Profile")

            except Exception as e:
                print(e)            

    return render(request, 'cv/form_profile.html', {'form': form})

def schedule(request):
    return render(request, 'schedule/schedule.html', {})
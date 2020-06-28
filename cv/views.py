from . import forms
from . import models
from django.shortcuts import (render, get_object_or_404)
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied


def profile(request):
    # profile = models.Profile.objects.all()
    return render(request, 'cv/profile.html', {})

def edit(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    if request.method == "POST":
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("Profile")
    elif request.method == "GET":
        profile = models.Profile.objects.first()

        if not (profile is None):
            form = forms.ProfileForm.objects.first()
        else:
            form = forms.ProfileForm()

    return render(request, 'cv/form_profile.html', {'form': form})

def schedule(request):
    return render(request, 'schedule/schedule.html', {})
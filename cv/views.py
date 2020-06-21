from django.shortcuts import render


def profile(request):
    return render(request, 'cv/profile.html', {})

def cv_edit(request):
    return render(request, 'cv/form_profile.html', {})

def schedule(request):
    return render(request, 'schedule/schedule.html', {})
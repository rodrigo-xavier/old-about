from django.shortcuts import render


@login_required
def profile(request):
    return render(request, 'cv/profile.html', {})
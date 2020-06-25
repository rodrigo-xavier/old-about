from django.shortcuts import render


def admin(request):
    return render(request, 'admin/admin.html', {})

def login(request):
    return render(request, 'admin/login.html', {})
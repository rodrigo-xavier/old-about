from . import views
from django.urls import path, re_path

app_name = 'cv'

urlpatterns = [
    path('profile/', views.profile, name="Profile"),
]
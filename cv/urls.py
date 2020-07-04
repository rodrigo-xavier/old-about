from . import views
from django.urls import path, re_path

app_name = 'cv'

urlpatterns = [
    path('', views.profile, name="Profile"),
    path('cv/edit/profile', views.edit_profile, name="Edit Profile"),
    path('cv/edit/xp', views.edit_xp, name="Edit XP"),
    path('schedule/', views.schedule, name="Schedule"),
]
from . import views
from django.urls import path, re_path

app_name = 'cv'

urlpatterns = [
    path('', views.profile, name="Profile"),
    path('cv/edit/', views.cv_edit, name="Edit"),
    path('schedule/', views.schedule, name="Schedule"),
]
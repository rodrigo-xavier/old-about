from . import views
from django.urls import path, re_path

app_name = 'Blog'

urlpatterns = [
    path('blog/', views.blog_list, name="Blog"),
]
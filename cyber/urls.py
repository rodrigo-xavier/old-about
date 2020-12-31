"""cyber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.conf.urls import (include, handler400, handler403, handler404, handler500)
    
from django.views.generic.base import RedirectView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('cv.urls', namespace="CV")),
    path('blog/', include('blog.urls', namespace="Blog")),
    path('admin/', views.admin, name="Admin"),
    path('root/', admin.site.urls, name="root"),

    path('root/', RedirectView.as_view(url='/root'), name='super-user')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
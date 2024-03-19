"""
URL configuration for relazion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home import views as _home 
from login import views as _login
from django.conf import settings # NEW
from django.conf.urls.static import static
from base import views as _base

urlpatterns = [
    path('',_home.index,name=""),
    path('login/',_login.index,name="login"),
    path('admin/', admin.site.urls)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
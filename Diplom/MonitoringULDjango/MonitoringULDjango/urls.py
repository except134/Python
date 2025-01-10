"""
Definition of urls for MonitoringULDjango.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', include('app.urls')),  
    path('admin/', admin.site.urls),
]

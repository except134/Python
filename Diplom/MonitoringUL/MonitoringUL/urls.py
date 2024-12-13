"""
Definition of urls for MonitoringUL.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from monitoring import forms, views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monitoring.urls')),  
]

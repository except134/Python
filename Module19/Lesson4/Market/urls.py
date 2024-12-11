from django.urls import path, include
from django.contrib import admin
from task1 import forms, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task1.urls')),  
]

from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.get_inn_from_html, name='get_inn_from_html'),
]


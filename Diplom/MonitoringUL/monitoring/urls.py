from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', maintpl.as_view(), maintpl.context),
]


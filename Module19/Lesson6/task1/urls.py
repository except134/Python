from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('createdb/', views.create_test_db, name='createdb'),
    path('html_sign_up/', views.sign_up_by_html, name='html_sign_up'),
    path('django_sign_up/', views.sign_up_by_django, name='django_sign_up'),
    path('', platformtpl.as_view(), platformtpl.context),
    path('platform/games/', gamestpl.as_view(), gamestpl.context),
    path('platform/cart/', carttpl.as_view(), carttpl.context),
    path('platform/news/', views.get_news, name='get_news'),
]


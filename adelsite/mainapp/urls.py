from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('woman/', woman, name='woman'),
    path('man/', man, name='man'),
    path('become/', become, name='become'),
    path('contacts/', contacts, name='contacts'),
    path('school/', school, name='school'),
]
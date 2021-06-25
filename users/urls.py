from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('registro', registro, name='registro'),
    path('logout_view', logout_view, name='logout_view'),
]

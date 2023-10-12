from django.urls import path
from django.contrib import auth
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
]
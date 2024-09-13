

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('Refresh', views.Refresh.as_view(), name='Refresh')
]

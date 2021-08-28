"""
my github: https://github.com/ruslancho
my email: r.melkovskiy@ukr.net
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^', views.index, name='index'),
]

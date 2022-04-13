from django.shortcuts import render
from django.urls import path, include
from .api import RegisterApi

#Register API
urlpatterns = [
      path('api/register', RegisterApi.as_view()),
]



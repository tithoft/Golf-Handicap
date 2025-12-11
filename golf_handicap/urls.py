"""Defines URL patterns for golf_handicap."""

from django.urls import path

from . import views

app_name = 'golf_handicap'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page showing golf courses played
    path('courses/', views.courses, name='courses'),
]

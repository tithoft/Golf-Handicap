"""Defines URL patterns for golf_handicap."""

from django.urls import path

from . import views

app_name = 'golf_handicap'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page showing golf courses played
    path('courses/', views.courses, name='courses'),
    # Page showing course information & scores at course
    path('courses/<int:course_id>/', views.course, name='course'),
    # Page for adding a new golf course.
    path('new_course/', views.new_course, name='new_course'),
    # Page for adding course information.
    path('new_tee/<int:course_id>/', views.new_tee, name='new_tee'),
    # Page for editing golf tee.
    path('edit_tee_tee/<int:tee_id>/', views.edit_tee, name='edit_tee'),
]

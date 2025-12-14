from django import forms

from .models import Course, CourseTee

class CourseForm(forms.ModelForm):
    """Form for adding golf course."""
    class Meta:
        model = Course
        fields = ['course_name', 'location']

class CourseTeeForm(forms.ModelForm):
    """Form for adding course information."""
    class Meta:
        model = CourseTee
        fields = ['tee_name', 'course_rating', 'slope_rating', 'course_par']
        
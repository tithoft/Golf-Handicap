from django.shortcuts import render

from .models import Course

def index(request):
    """Home page for Golf Handicap."""
    return render(request, 'golf_handicap/index.html')

def courses(request):
    """Show all courses user played."""
    courses = Course.objects.order_by('course_name')
    context = {'courses': courses}
    return render(request, 'golf_handicap/courses.html', context)
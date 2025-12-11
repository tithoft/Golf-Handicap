from django.shortcuts import render

from .models import Course, CourseTee

def index(request):
    """Home page for Golf Handicap."""
    return render(request, 'golf_handicap/index.html')

def courses(request):
    """Show all courses user played."""
    courses = Course.objects.order_by('course_name')
    context = {'courses': courses}
    return render(request, 'golf_handicap/courses.html', context)

def course(request, course_id):
    """Show information about a singel course and scores from course."""
    course = Course.objects.get(id=course_id)
    tees = course.coursetee_set.order_by('slope_rating')
    context = {'course': course, 'tees': tees}
    return render(request, 'golf_handicap/course.html', context)


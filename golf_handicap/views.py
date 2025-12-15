from django.shortcuts import render, redirect

from .models import Course, CourseTee
from .forms import CourseForm, CourseTeeForm

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

def new_course(request):
    """Add a new course."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CourseForm()
    else:
        # POST data submitted; process data.
        form = CourseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('golf_handicap:courses')
        
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'golf_handicap/new_course.html', context)

def new_tee(request, course_id):
    """Add new course tee for individual course."""
    course = Course.objects.get(id=course_id)

    if request.method != 'POST':
        # No data submitted; creat a blank form.
        form = CourseTeeForm()
    else:
        # POST data submitted; process data.
        form = CourseTeeForm(data=request.POST)
        if form.is_valid():
            new_tee = form.save(commit=False)
            new_tee.course = course
            new_tee.save()
            return redirect('golf_handicap:course', course_id=course_id)
        
    # Display a blank or invalid form.
    context = {'course': course, 'form': form}
    return render(request, 'golf_handicap/new_tee.html', context)

def edit_tee(request, tee_id):
    """Edit an existingn course tee."""
    tee = CourseTee.objects.get(id=tee_id)
    course = tee.course
    if request.method != 'POST':
        # Initial request; pre-fill form with the current course tee.
        form = CourseTeeForm(instance=tee)
    else:
        # POST data submitted; process data.
        form = CourseTeeForm(instance=tee, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('golf_handicap:course', course_id=course.id)
    context = {'tee': tee, 'course': course, 'form': form}
    return render(request, 'golf_handicap/edit_tee.html', context)


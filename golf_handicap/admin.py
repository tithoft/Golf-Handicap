from django.contrib import admin

from .models import Course, CourseTee, Score

admin.site.register(Course)
admin.site.register(CourseTee)
admin.site.register(Score)
from django.contrib import admin

from authentication.models import Student
from vege.models import Recipe, Department, StudentId, Students, Subject, SubjectMarks

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Students)
admin.site.register(Subject)

class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']
admin.site.register(SubjectMarks, SubjectMarksAdmin)
from django.contrib import admin

from authentication.models import Student
from vege.models import Recipe, Department, StudentId, Students

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Students)
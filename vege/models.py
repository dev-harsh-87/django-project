from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True , blank=True )
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipe_images')

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department

    class Meta:
        ordering = ['department']

class StudentId(models.Model):
    student_id = models.CharField(max_length=100)
    def __str__(self):
        return self.student_id
    class Meta:
        ordering = ['student_id']

class Students(models.Model):
    student_id = models.OneToOneField(StudentId, on_delete=models.SET_NULL, null=True , blank=True )
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True , blank=True )
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField(default=18)
    student_email = models.EmailField(unique=True)
    student_address = models.TextField()


    def __str__(self) -> str:
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = 'student'


class SubjectMarks(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='studentmarks')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,)
    marks = models.IntegerField()

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return f'{self.student.student_name} - {self.subject.subject_name}'



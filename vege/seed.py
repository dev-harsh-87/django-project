from faker import Faker
from faker.generator import random

from authentication.models import Student
from vege.models import Department
from .models import *

fake = Faker()

def seed_marks(n):
    try:
        student_data = Students.objects.all()
        for student in student_data:
            subject_data = Subject.objects.all()
            for subject in subject_data:
                SubjectMarks.objects.create(student=student, subject=subject, marks=random.randint(1, 100))
    except Exception as e:
        print(e)

def seed_db(n=10) -> None:
   try:
       for _ in range(0, n):
           department_data = Department.objects.all()
           department_random_index = random.randint(0, len(department_data)-1)
           department = department_data[department_random_index]
           student_id = f"STU-0{random.randint(1, 100)}"
           student_name = fake.name()
           student_age = random.randint(18, 26)
           student_email = fake.email()
           student_address = fake.address()

           student_id_obj = StudentId.objects.create(
               student_id=student_id,

           )

           Students.objects.create(
               student_id=student_id_obj,
               student_name=student_name,
               department=department,
               student_age=student_age,
               student_email=student_email,
               student_address=student_address,
           )


   except Exception as e:
       print(e)
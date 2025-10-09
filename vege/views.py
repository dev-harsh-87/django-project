from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from authentication.models import Student
from vege.models import Recipe, Students, SubjectMarks
from django.db.models import Q, Sum


@login_required(login_url='/login')
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")  # <-- FILES for image

        print(recipe_name)
        print(recipe_description)
        print(recipe_image)  # This will print InMemoryUploadedFile object
        print(f"Form data: {data}")

        Recipe.objects.create(recipe_name=recipe_name,recipe_description=recipe_description,recipe_image=recipe_image)

        return redirect("/recipes")
    recipe_data = Recipe.objects.all()
    if request.GET.get('search_text'):
        recipe_data = recipe_data.filter(recipe_name__icontains=request.GET.get('search_text'))
    context = {"recipeData": recipe_data}
    return render(request, "recipes.html", context)

def recipe_delete(request, recipe_id):
    recipe = Recipe.objects.get(id = recipe_id)
    recipe.delete()
    return redirect("/recipes")

def recipe_edit(request, recipe_id):
    recipe = Recipe.objects.get(id = recipe_id)
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        recipe.recipe_name = recipe_name
        recipe.recipe_description = recipe_description
        if recipe_image:
            recipe.recipe_image = recipe_image
        recipe.save()
        return redirect("/recipes")

    context = {"recipeData": recipe}
    return render(request, "update-recipe.html", context)


def get_students(request):

    students = Students.objects.all().order_by('id')

    if request.GET.get('search_text'):
        students = students.filter(
            Q(student_name__icontains=request.GET.get('search_text')) |
            Q(department__department__icontains=request.GET.get('search_text')),)

    paginator = Paginator(students, 12)  # Show 5 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return  render(request, 'students.html', context)

def get_student_details(request, student_id):
    student_marks = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = student_marks.aggregate(total_marks=Sum('marks'))
    return render(request, 'student-details.html', {'student_marks': student_marks , 'total_marks': total_marks})
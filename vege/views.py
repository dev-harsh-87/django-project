from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from vege.models import Recipe

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


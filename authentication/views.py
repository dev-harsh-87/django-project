from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render, redirect


# Create your views here.


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/login')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Username or password is incorrect')
            return redirect('/login')
        else:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('home')


    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        print(f"user data is : {username}, {email}, {password}")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/register')

        # Store data in the database
        user = User.objects.create(
            username=username,
            email=email,
        )
        user.set_password(password)  # Encrypt password
        user.save()

        messages.success(request, "User registered successfully!")
        return redirect('/login')  # Or wherever you want

    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('/login')
@login_required(login_url='/login')
def user_profile(request):
    user_data = request.user  # get the currently logged-in user
    user_recipes = request.user.recipe_set.all()  # assuming Recipe model has FK to User

    print(user_recipes)

    return render(request, 'profile.html', {
        'user_data': user_data,
        'user_recipes': user_recipes
    })
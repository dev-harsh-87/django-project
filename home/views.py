from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    peoples = [
        {"name": "James", "age": 28, "date": "10/01/2025"},
        {"name": "Emily", "age": 25, "date": "10/02/2025"},
        {"name": "Michael", "age": 32, "date": "10/03/2025"},
        {"name": "Olivia", "age": 27, "date": "10/04/2025"},
        {"name": "William", "age": 30, "date": "10/05/2025"},
        {"name": "Sophia", "age": 24, "date": "10/06/2025"},
        {"name": "Benjamin", "age": 29, "date": "10/07/2025"},
        {"name": "Isabella", "age": 26, "date": "10/08/2025"},
        {"name": "Alexander", "age": 31, "date": "10/09/2025"},
        {"name": "Mia", "age": 23, "date": "10/10/2025"},
    ]

    return render(request, "index.html", {"peoples": peoples})


#  pass page name in context to change name dynamic when we user that page
# def baseview(request):
#     context = {'page' : 'baseview'}
#     return render(request, "base.html")
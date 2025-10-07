from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from authentication.models import Student
from vege.models import Students


# Create your views here.
@login_required(login_url='/login')
def home(request):
    students = Students.objects.all().order_by('id')
    paginator = Paginator(students, 20)  # Show 5 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {'page_obj': page_obj})


#  pass page name in context to change name dynamic when we user that page
# def baseview(request):
#     context = {'page' : 'baseview'}
#     return render(request, "base.html")

# IP : 192.168.29.80

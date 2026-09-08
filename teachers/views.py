from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from teachers.models import Teacher

# Create your views here.

def teachers_list(request):
    return render(request, 'teachers/teacher_list.html')

def teachers_detail(request):
    return render(request, 'teachers/teacher_detail.html')

def teachers_home(request):
    return render(request, 'teachers/home.html')

def index(request):
    return render(request, 'teachers/index.html')

def add_teacher(request):
    return render(request, 'teachers/add_teacher.html')
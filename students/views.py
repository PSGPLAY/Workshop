from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer


def students_home(request):
    return render(request, 'home.html')


def students_about(request):
    return render(request, 'about.html')


students = [
    {
        "student_id": 1,
        "name": "Kaushal Karn",
        "age": 20,
        "grade": "A",
        "course": "Computer Science"
    },
    {
        "student_id": 2,
        "name": "John Doe",
        "age": 22,
        "grade": "B",
        "course": "Mathematics"
    },
    {
        "student_id": 3,
        "name": "Harry Potter",
        "age": 20,
        "grade": "A",
        "course": "Computer Science"
    },
    {
        "student_id": 4,
        "name": "Jane Smith",
        "age": 19,
        "grade": "B",
        "course": "Physics"
    }
]


def student_display(request):
    """
    Returns the old hard-coded student data as JSON.
    """
    return JsonResponse(students, safe=False)


def student_detail_old(request, student_id):
    """
    Finds a student from the old hard-coded list.
    This is kept only if you still need the old API example.
    """

    for student in students:
        if student["student_id"] == student_id:
            return JsonResponse(student)

    return HttpResponse("Student not found.")

def student_list(request):
    """
    Displays all students from the database.
    """

    students = Student.objects.all()

    context = {
        'page_title': 'Student List',
        'students': students,
        'total_students': students.count(),
        'current_date': datetime.now(),
        'user': request.user,
    }

    return render(
        request,
        'students/student_list.html',
        context
    )


def student_detail(request, student_id):
    """
    Displays one student from the database.

    Example:
        /students/student/1/
    """

    student = get_object_or_404(
        Student,
        id=student_id
    )

    context = {
        'student': student,
    }

    return render(
        request,
        'students/student_detail.html',
        context
    )



def index(request):
    return render(
        request,
        'students/index.html'
    )

def add_student(request):

    Student.objects.create(
        student_id=12,
        first_name='sheloi',
        last_name='syadav',
        email='saon1i12q3@gmail.com',
        phone='9876542222',
        date_of_birth='2006-05-23',
        department='csit',
        semester='spring 2026',
        status='active',
        address='morang',
        notes='django'
    )

    return render(
        request,
        'students/add_student.html'
    )

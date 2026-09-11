from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Student, Enrollment
from .forms import StudentForm, EnrollmentForm
from .serializers import StudentSerializer


def students_home(request):
    return render(request, 'home.html')


def students_about(request):
    return render(request, 'about.html')


def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )

def student_detail(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":

        enrollment_form = EnrollmentForm(
            request.POST,
            student=student
        )

        if enrollment_form.is_valid():

            enrollment = enrollment_form.save(commit=False)

            enrollment.student = student

            enrollment.save()

            return redirect(
                "students:student_details",
                student_id=student.id
            )

    else:

        enrollment_form = EnrollmentForm(
            student=student
        )

    return render(
        request,
        "students/student_details.html",
        {
            "student": student,
            "enrollment_form": enrollment_form,
        }
    )



def index(request):
    students = Student.objects.all()

    active_students = students.filter(status="active")
    inactive_students = students.filter(status="inactive")

    departments = students.values("department").distinct()

    context = {
        "students": students,
        "total_student": students.count(),
        "active_student": active_students.count(),
        "inactive_student": inactive_students.count(),
        "departments": departments.count(),
    }

    return render(
        request,
        "students/index.html",
        context
    )


def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            student = form.save()

            return redirect(
                "students:student_details",
                student_id=student.id
            )

    else:

        form = StudentForm()

    return render(
        request,
        "students/add_student.html",
        {
            "form": form
        }
    )


def delete_student(request, student_id):
    student = get_object_or_404(Student, id= student_id)

    if request.method == "POST":
        student.delete()
        return redirect("students:student_list")

    return render(request, "students/delete_student.html", {"student": student})
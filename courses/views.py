from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from .models import Course
from .forms import CourseForm


def course_display(request):
    return HttpResponse("This is the course display page.")


def courses(request):
    courses_list = Course.objects.all()

    return render(request, "courses.html", {
        "courses": courses_list
    })


def course_details(request, id):
    course = Course.objects.get(id=id)

    return render(request, "course-details.html", {
        "course": course
    })


def index(request):
    courses_list = Course.objects.all()

    active_course = courses_list.filter(status="active")
    inactive_course = courses_list.filter(status="inactive")

    departments = Course.objects.values("department").distinct()

    context = {
        "courses": courses_list,
        "total_course": courses_list.count(),
        "active_course": active_course.count(),
        "inactive_course": inactive_course.count(),
        "departments": departments.count(),
    }

    return render(request, "index.html", context)


def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("courses:courses")

    else:
        form = CourseForm()

    return render(request, "add_course.html", {
        "form": form
    })


def delete_course(request, course_id):
    course = get_object_or_404(Course, id = course_id)

    if request.method == "POST":
        course.delete()
        return redirect("courses:courses")

    return render(request, "courses/delete_course.html", {"course": course})


def update_course(request, course_id):
    course = get_object_or_404(Course, id= course_id)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)

        if form.is_valid():
            form.save()
            return redirect("courses:course_details", course_id=course.id)
    else:
        form = CourseForm(instance=course)

    return render(request, "add_course.html", {"form":form, "course":course})
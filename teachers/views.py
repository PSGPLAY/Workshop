from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from .forms import TeacherForm


def teachers_list(request):
    teachers = Teacher.objects.all()

    return render(
        request,
        "teachers/teacher_list.html",
        {"teachers": teachers}
    )


def teachers_detail(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    return render(
        request,
        "teachers/teacher_detail.html",
        {"teacher": teacher}
    )


def teachers_home(request):
    return render(
        request,
        "teachers/home.html"
    )


def index(request):
    teachers_list = Teacher.objects.all()

    active_teacher = teachers_list.filter(status="active")
    inactive_teacher = teachers_list.filter(status="inactive")
    departments = Teacher.objects.values("department").distinct()

    context = {
        "teachers": teachers_list,
        "total_teacher": teachers_list.count(),
        "active_teacher": active_teacher.count(),
        "inactive_teacher": inactive_teacher.count(),
        "departments": departments.count(),
    }

    return render(
        request,
        "teachers/index.html",
        context
    )


def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("teachers:teachers")

    else:
        form = TeacherForm()

    return render(
        request,
        "teachers/add_teacher.html",
        {"form": form}
    )

def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == "POST":
        teacher.delete()
        return redirect("teachers:teachers")

    return render(request, "teachers/delete_teacher.html", {"teacher":teacher})


def update_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect("teachers:teacher_detail", id=teacher.id)
    else:
        form=TeacherForm(instance=teacher)

    return render(request, "teachers/add_teacher.html", {"form":form, "teacher":teacher})



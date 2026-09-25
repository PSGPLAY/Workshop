from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone


from students.models import Student
from courses.models import Course

from .models import Attendance
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def home(request):
    return HttpResponse("HELLO")

@login_required
def attendance_list(request):
    today = timezone.localdate()

    date_string = request.GET.get("date")

    if date_string:
        try:
            selected_date=datetime.strptime(date_string, "%Y-%m-%d").date()
        except ValueError:
            selected_date=today
    else:
        selected_date=today

    attendance = (
        Attendance.objects
        .filter(date=selected_date)
        .select_related(
            "student",
            "course",
            "course__instructor",
        )
    )

    courses = Course.objects.all()

    search = request.GET.get("search")
    if search:
        attendance = attendance.filter(
            Q(student__first_name__icontains=search) | Q(student__last_name__icontains=search) | Q(student__student_id__icontains=search)
        )

    course_id = request.GET.get("course")
    if course_id:
        attendance = attendance.filter(course_id=course_id)

    status = request.GET.get("status")
    if status:
        attendance = attendance.filter(status=status)

    total_students = Student.objects.count()
    present_count = attendance.filter(status="present").count()
    absent_count = attendance.filter(status="absent").count()
    late_count = attendance.filter(status="late").count()

    context = {
        "attendance": attendance,
        "today": today,
        "selected_date": selected_date,
        "courses": courses,
        "total_students": total_students,
        "present_count": present_count,
        "absent_count": absent_count,
        "late_count": late_count,
    }

    return render(
        request,
        "attendance/attendance.html",
        context,
    )

@login_required
def take_attendance(request):

    courses = Course.objects.all()

    selected_course = None
    students = []

    # Always start with today's date as a Python date object
    selected_date = timezone.localdate()

    # -------------------------
    # GET - Show students
    # -------------------------
    if request.method == "GET":

        course_id = request.GET.get("course")
        date_string = request.GET.get("date")

        # Convert the date string into a Python date object
        if date_string:
            try:
                selected_date = datetime.strptime(
                    date_string,
                    "%Y-%m-%d"
                ).date()
            except ValueError:
                selected_date = timezone.localdate()

        if course_id:

            selected_course = get_object_or_404(
                Course,
                id=course_id
            )

            students = Student.objects.filter(
                enrollments__course=selected_course,
                enrollments__status="Enrolled"
            ).distinct()

            existing_attendance = Attendance.objects.filter(
                course=selected_course,
                date=selected_date
            )

            attendance_map = {
                record.student_id: record.status
                for record in existing_attendance
            }

            for student in students:

                student.attendance_status = attendance_map.get(
                    student.id,
                    "present"
                )

    # -------------------------
    # POST - Save attendance
    # -------------------------
    elif request.method == "POST":

        course_id = request.POST.get("course")
        date_string = request.POST.get("date")

        selected_course = get_object_or_404(
            Course,
            id=course_id
        )

        # Convert submitted date into a Python date
        if date_string:
            try:
                selected_date = datetime.strptime(
                    date_string,
                    "%Y-%m-%d"
                ).date()
            except ValueError:
                selected_date = timezone.localdate()
        else:
            selected_date = timezone.localdate()

        students = Student.objects.filter(
            enrollments__course=selected_course,
            enrollments__status="Enrolled"
        ).distinct()

        for student in students:

            status = request.POST.get(
                f"status_{student.id}"
            )

            if status:

                Attendance.objects.update_or_create(
                    student=student,
                    course=selected_course,
                    date=selected_date,
                    defaults={
                        "status": status
                    }
                )

        return redirect(
            "attendance:attendance"
        )

    context = {
        "courses": courses,
        "selected_course": selected_course,
        "selected_date": selected_date,
        "students": students,
    }

    return render(
        request,
        "attendance/take_attendance.html",
        context
    )


def attendance_history(request):

    attendance = (
        Attendance.objects
        .all()
        .select_related(
            "student",
            "course",
            "course__instructor",
        )
        .order_by("-date", "student__name")
    )

    courses = Course.objects.all()

    # Search student
    search = request.GET.get("search")

    if search:
        attendance = attendance.filter(
            student__name__icontains=search
        )

    # Course filter
    course_id = request.GET.get("course")

    if course_id:
        attendance = attendance.filter(
            course_id=course_id
        )

    # Status filter
    status = request.GET.get("status")

    if status:
        attendance = attendance.filter(
            status=status
        )

    # Date filter
    date = request.GET.get("date")

    if date:
        attendance = attendance.filter(
            date=date
        )

    context = {
        "attendance": attendance,
        "courses": courses,
    }

    return render(
        request,
        "attendance/attendance_history.html",
        context
    )



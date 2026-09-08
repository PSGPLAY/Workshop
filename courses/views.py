from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Course
from django.contrib import messages

from teachers.models import Teacher

from django.contrib.auth.decorators import login_required

def course_display(request):
    return HttpResponse("This is the course display page.")

@login_required
def courses(request):
    return render(request, 'courses.html')

def course_details(request):
    return render(request, 'course-details.html')

def index(request):
    courses_list =Course.objects.all()
    active_course=courses_list.filter(status='active')
    inactive_course=courses_list.filter(status='inactive')
    departments = Course.objects.values('department').distinct()
   
    context = {
        'courses':courses_list,
        'total_course': courses_list.count(),
        'active_course': active_course.count(),
        'inactive_course': inactive_course.count(),
        'departments':len(departments),
        }
    return render(request, 'index.html')

def add_course(request):
    teachers = Teacher.objects.filter(status="active")

    if request.method == "POST":
        Course.objects.create(
            code=request.POST.get("code"),
            name=request.POST.get("name"),
            department=request.POST.get("department"),
            instructor_id=request.POST.get("instructor"),
            credits=request.POST.get("credits"),
            duration=request.POST.get("duration"),
            semester=request.POST.get("semester"),
            capacity=request.POST.get("capacity"),
            status=request.POST.get("status"),
            description=request.POST.get("description"),
        )
        messages.success(request, "Course added successfully.")
        return redirect('courses:courses')

    return render(request, "add_course.html", {"teachers": teachers}
    )
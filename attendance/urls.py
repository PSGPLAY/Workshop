from django.urls import path

from . import views


app_name = "attendance"


urlpatterns = [
    path(
        "",
        views.attendance_list,
        name="attendance",
    ),

    path(
        "attendance-list/",
        views.attendance_list,
        name="attendance_list",
    ),

    path(
        "take-attendance/",
        views.take_attendance,
        name="take_attendance",
    ),

    path(
        "attendance-history/",
        views.attendance_history,
        name="attendance_history",
    ),
]
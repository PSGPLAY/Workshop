from django.urls import path
from . import views


app_name = 'students'


urlpatterns = [

    # Student list
    path(
        'student_list/',
        views.student_list,
        name='student_list'
    ),

    # Index
    path(
        'index/',
        views.index,
        name='index'
    ),

    # Student detail
    path(
        'student/<int:student_id>/',
        views.student_detail,
        name='student_details'
    ),

    # Add student
    path(
        'add-student/',
        views.add_student,
        name='add_student'
    ),

]

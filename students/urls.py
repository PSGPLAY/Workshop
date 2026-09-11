from django.urls import path
from . import views


app_name = 'students'


urlpatterns = [

    path('student_list/',views.student_list,name='student_list'),
    path('index/',views.index,name='index'),
    path('student/<int:student_id>/',views.student_detail,name='student_details'),
    path('add-student/',views.add_student,name='add_student'),
    path('student/<int:student_id>/delete/', views.delete_student, name='delete_student')
]

from django.urls import path
from .import views

app_name='teachers'

urlpatterns = [
      path('index/', views.index, name='index'),
      path('teacher-list/', views.teachers_list, name='teachers'),
      path('teacher/<int:id>', views.teachers_detail, name='teacher_detail'),
      path('add-teacher/', views.add_teacher, name='add_teacher'),
      path('teacher/delete_teacher/<int:teacher_id>', views.delete_teacher, name='delete_teacher'),
      path('teacher/update_teacher/<int:teacher_id>', views.update_teacher, name="update_teacher"),
]
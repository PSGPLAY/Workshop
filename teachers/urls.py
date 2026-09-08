from django.urls import path
from .import views

app_name='teachers'

urlpatterns = [
      path('index/', views.index, name='index'),
      path('teacher-list/', views.teachers_list, name='teachers'),
      path('teacher/', views.teachers_detail, name='teacher_detail'),
      path('add-teacher/', views.add_teacher, name='add_teacher'),

]
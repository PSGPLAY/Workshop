from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, ProjectViewSet, DashboardView, CompletedTaskListView, LoginView

router = DefaultRouter()
# tasks/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LoginView, TaskViewSet, ProjectViewSet


router = DefaultRouter()

router.register(
    r'tasks',
    TaskViewSet,
    basename='tasks'
)

router.register(
    r'projects',
    ProjectViewSet,
    basename='projects'
)


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('tasks/completed/', CompletedTaskListView.as_view(), name='completed-tasks'),
]
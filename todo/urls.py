from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='home'),  # todo.home
    path('tasks/<slug>/', views.task_detail, name='task_detail'),
]

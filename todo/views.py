from django.shortcuts import render

from todo.models import Task


def home(request):
    num_tasks = Task.objects.count()
    tasks = Task.objects.all()
    return render(request, './todo/home.html', {'num_tasks': num_tasks, 'tasks': tasks})


def task_detail(request, slug):
    task = Task.objects.get(slug=slug)
    return render(request, 'todo/tasks/detail.html', dict(task=task))

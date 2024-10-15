from django.shortcuts import redirect, render
from django.utils.text import slugify

from todo.models import Task

from .forms import AddTaskForm


def home(request):
    num_tasks = Task.objects.count()
    tasks = Task.objects.all()
    return render(request, './todo/home.html', {'num_tasks': num_tasks, 'tasks': tasks})


def task_detail(request, slug):
    task = Task.objects.get(slug=slug)
    return render(request, 'todo/tasks/detail.html', dict(task=task))


def add_task(request):
    if request.method == 'POST':
        if (form := AddTaskForm(request.POST)).is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect('todo:home')
    else:
        form = AddTaskForm()

    return render(request, 'todo/add_task.html', dict(form=form))

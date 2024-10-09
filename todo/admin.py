from django.contrib import admin

from .models import Task


# @admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'task_made',
        'created_at',
    ]
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Task, TaskAdmin)

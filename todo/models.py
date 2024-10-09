from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    task_made = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, default='')

    def __str__(self):
        return self.title

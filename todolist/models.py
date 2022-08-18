from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    title = models.CharField(max_length=100)
    tasks = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

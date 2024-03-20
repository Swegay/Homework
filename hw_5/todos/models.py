from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'ID: {self.id} - {self.title}'


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'ID: {self.id} - {self.title}'

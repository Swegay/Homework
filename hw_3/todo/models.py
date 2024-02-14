from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    due_date = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'ID: {self.id} {self.title}'

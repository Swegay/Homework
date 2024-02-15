from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    due_date = models.DateTimeField(null=True)
    status = models.BooleanField(null=True, blank=True, default=False)
    objects = models.Manager()

    def __str__(self):
        return f'ID: {self.id} - {self.title}'

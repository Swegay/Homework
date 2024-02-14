# Generated by Django 5.0.1 on 2024-02-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0003_alter_todo_due_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="due_date",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="todo",
            name="status",
            field=models.BooleanField(default=False),
        ),
    ]

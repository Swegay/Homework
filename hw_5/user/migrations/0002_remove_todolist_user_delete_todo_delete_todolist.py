# Generated by Django 5.0.2 on 2024-03-20 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todolist",
            name="user",
        ),
        migrations.DeleteModel(
            name="Todo",
        ),
        migrations.DeleteModel(
            name="TodoList",
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0003_delete_todos"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="due_date",
            field=models.DateTimeField(),
        ),
    ]

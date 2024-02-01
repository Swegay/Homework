from django.apps import AppConfig


class MyDatabaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_database'

from django.contrib import admin
from django.urls import path

from .views import get_index_page, get_todo_details

urlpatterns = [
    path('', get_index_page),
    path('todo/<int:pk>', get_todo_details)
]
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from .views import get_index_page, todos_page_view, delete_todo

urlpatterns = [
    path('', get_index_page),
    path('add/', get_index_page),
    path('todos/', todos_page_view, name='todos_page'),
    path('todos/<int:pk>/delete', delete_todo)
]

from django.urls import path
from .views import index_page_view, todo_lists_page_view, todo_list_detail_view, delete_todo_list_view, \
    edit_todo_list_view, delete_todo_view, edit_todo_view, create_todo_view, get_todo_details

urlpatterns = [

    path('', todo_lists_page_view, name='index_page'),
    path('todo/<int:id>', get_todo_details, name='todo-details'),
    path('create-todo/', create_todo_view, name='create_todo'),
    path('todo-lists/', todo_lists_page_view, name='todo-lists'),
    path('todo-lists/<int:id>', todo_list_detail_view, name='todo-list-detail'),
    path('todo-lists/<int:id>/delete', delete_todo_list_view, name='delete_todo_list'),
    path('todo-lists/<int:id>/edit', edit_todo_list_view, name='edit_todo_list'),
    path('todos/<int:id>/delete', delete_todo_view, name='delete_todo'),
    path('todos/<int:id>/edit', edit_todo_view, name='edit_todo'),
]

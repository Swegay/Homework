from django.urls import path
from .views import login_view, logout_view, register_view, forgot_password_view, get_user_todos, get_user_todo_details, \
    create_user_todo, delete_user_todo

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('todos/', get_user_todos, name='user_todos'),
    path('todos/<int:id>/', get_user_todo_details, name='user_todo_details'),
    path('todos/create/', create_user_todo, name='create_user_todo'),
    path('todos/<int:id>/delete/', delete_user_todo, name='delete_user_todo'),
]
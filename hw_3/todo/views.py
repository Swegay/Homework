from django.shortcuts import render
from .models import Todo

def get_index_page(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def get_todo_details(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_details.html', {'todo': todo})

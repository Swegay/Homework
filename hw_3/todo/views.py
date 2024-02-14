from django.shortcuts import render, redirect
from .models import Todo
from .forms import CreateTodoForm


def get_index_page(request):
    all_todos = Todo.objects.all()
    return render(request, 'todo/todos.html', {'all_todos': all_todos})


def get_todo_details(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo-details.html', {'todo': todo})


def todos_page_view(request):
    if request.method == 'GET':
        form = CreateTodoForm()
        all_todos = Todo.objects.all()
        return render(request, 'todo/index.html', {'all_todos': all_todos, 'form': form})
    if request.method == 'POST':
        form = CreateTodoForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            due_date = form.cleaned_data.get('due_date')
            status = form.cleaned_data.get('status', False)
            todo = Todo(title=title, description=description, due_date=due_date, status=status)
            todo.save()
        todos = Todo.objects.all()
        return render(request, 'todo/index.html', {'todos': todos, 'form': form})



def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect('/todos')
    except Todo.DoesNotExist:
        return redirect('/todos')

from django.shortcuts import render, redirect
from .models import TodoList, Todo
from .forms import CreateTodoListForm, CreateTodoForm


def index_page_view(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'todos/index.html', {'todo_lists': todo_lists})


def todo_lists_page_view(request):
    if request.method == 'GET':
        form = CreateTodoListForm()
        todo_lists = TodoList.objects.all()
        return render(request, 'todos/todo-lists.html', {'form': form, 'todo_lists': todo_lists})
    elif request.method == 'POST':
        form = CreateTodoListForm(request.POST)
        if form.is_valid():
            form.save()
        todo_lists = TodoList.objects.all()
        return render(request, 'todos/todo-lists.html', {'form': form, 'todo_lists': todo_lists})


def todo_list_detail_view(request, id):
    todo_list = TodoList.objects.get(id=id)
    todos = Todo.objects.filter(todo_list_id=id)
    return render(request, 'todos/todo-list-detail.html', {'todo_list': todo_list, 'todos': todos})


def delete_todo_list_view(request, id):
    todo_list = TodoList.objects.get(id=id)
    todo_list.delete()
    return redirect('todo-lists')


def edit_todo_list_view(request, id):
    todo_list = TodoList.objects.get(id=id)

    if request.method == 'GET':
        form = CreateTodoListForm(instance=todo_list)
        return render(request, 'todos/edit-todo-list.html', {'todo_list': todo_list, 'form': form})
    elif request.method == 'POST':
        form = CreateTodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo-lists')


def todos_page_view(request):
    if request.method == 'GET':
        form = CreateTodoForm()
        all_todos = Todo.objects.all()
        return render(request, 'todos/index.html', {'all_todos': all_todos, 'form': form})
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
        return render(request, 'todos/index.html', {'todos': todos, 'form': form})


def get_todo_details(request, id):
    todo = Todo.objects.get()
    return render(request, 'todos/todo-details.html', {'todo': todo})


def create_todo_view(request):
    if request.method == 'GET':
        form = CreateTodoForm()
        return render(request, 'todos/create-todo.html', {'form': form})
    elif request.method == 'POST':
        form = CreateTodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('index_page')

    return render(request, 'todos/create-todo.html', {'form': form})


def delete_todo_view(request, id):
    todo = Todo.objects.get(id=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('todo-list-detail', id=todo_list_id)


def edit_todo_view(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == 'GET':
        form = CreateTodoForm(instance=todo)
        return render(request, 'todos/edit-todo.html', {'todo': todo, 'form': form})
    elif request.method == 'POST':
        form = CreateTodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo-list-detail', id=todo.todo_list.id)

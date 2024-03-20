from django.shortcuts import render, redirect
from .models import TodoList, Todo
from .forms import CreateTodoListForm, CreateTodoForm
from django.contrib.auth.decorators import login_required


@login_required
def index_page_view(request):
    todo_lists = TodoList.objects.filter(user=request.user)
    return render(request, 'todos/index.html', {'todo_lists': todo_lists})


@login_required
def todo_lists_page_view(request):
    if request.method == 'GET':
        form = CreateTodoListForm()
        todo_lists = TodoList.objects.filter(user=request.user)
        return render(request, 'todos/todo-lists.html', {'form': form, 'todo_lists': todo_lists})
    elif request.method == 'POST':
        form = CreateTodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.user = request.user
            todo_list.save()
        return redirect('todo-lists')


@login_required
def todo_list_detail_view(request, id):
    todo_list = TodoList.objects.get(id=id)
    if todo_list.user == request.user:
        todos = Todo.objects.filter(todo_list_id=id)
        return render(request, 'todos/todo-list-detail.html', {'todo_list': todo_list, 'todos': todos})
    else:
        return redirect('index_page')


@login_required
def delete_todo_list_view(request, id):
    todo_list = TodoList.objects.get(id=id)
    if todo_list.user == request.user:
        todo_list.delete()
    return redirect('todo-lists')


@login_required
def edit_todo_list_view(request, id):
    todo_list = TodoList.objects.get(id=id)
    if todo_list.user == request.user:
        if request.method == 'GET':
            form = CreateTodoListForm(instance=todo_list)
            return render(request, 'todos/edit-todo-list.html', {'todo_list': todo_list, 'form': form})
        elif request.method == 'POST':
            form = CreateTodoListForm(request.POST, instance=todo_list)
            if form.is_valid():
                form.save()
                return redirect('todo-lists')
    else:
        return redirect('index_page')


@login_required
def todos_page_view(request):
    if request.method == 'GET':
        form = CreateTodoForm()
        all_todos = Todo.objects.filter(todo_list__user=request.user)
        return render(request, 'todos/index.html', {'all_todos': all_todos, 'form': form})
    elif request.method == 'POST':
        form = CreateTodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
        return redirect('index_page')


@login_required
def get_todo_details(request, id):
    todo = Todo.objects.get(id=id)
    if todo.user == request.user:
        return render(request, 'todos/todo-details.html', {'todo': todo})
    else:
        return redirect('index_page')


@login_required
def create_todo_view(request):
    if request.method == 'GET':
        form = CreateTodoForm(user=request.user)
        return render(request, 'todos/create-todo.html', {'form': form})
    elif request.method == 'POST':
        form = CreateTodoForm(request.user, request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
        return redirect('index_page')


@login_required
def delete_todo_view(request, id):
    todo = Todo.objects.get(id=id)
    if todo.user == request.user:
        todo.delete()
    return redirect('index_page')


@login_required
def edit_todo_view(request, id):
    todo = Todo.objects.get(id=id)
    if todo.user == request.user:
        if request.method == 'GET':
            form = CreateTodoForm(user=request.user, instance=todo)
            return render(request, 'todos/edit-todo.html', {'todo': todo, 'form': form})
        elif request.method == 'POST':
            form = CreateTodoForm(request.user, request.POST, instance=todo)
            if form.is_valid():
                form.save()
                return redirect('index_page')
    else:
        return redirect('index_page')

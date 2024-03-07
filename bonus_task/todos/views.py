from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Todo
from .forms import CreateTodoForm


def get_index_page(request):
    all_todos = Todo.objects.all()
    if request.method == 'GET':
        form = CreateTodoForm()
        return render(request, 'todos/index.html', {'all_todos': all_todos, 'form': form})
    elif request.method == 'POST':
        form = CreateTodoForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            due_date = form.cleaned_data.get('due_date')
            status = form.cleaned_data.get('status', False)
            todo = Todo(title=title, description=description, due_date=due_date, status=status)
            todo.save()
            all_todos = Todo.objects.all()
            return render(request, 'todos/index.html', {'all_todos': all_todos, 'form': form})


def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect('/todos')
    except Todo.DoesNotExist:
        return redirect('/todos')


def todos_page_view(request):
    all_todos = Todo.objects.all()

    title_filter = request.GET.get('title', '')
    due_date_filter = request.GET.get('due_date', '')

    if title_filter:
        all_todos = all_todos.filter(title__icontains=title_filter)
    if due_date_filter:
        all_todos = all_todos.filter(due_date__icontains=due_date_filter)

    items_per_page = request.GET.get('items_per_page', 5)
    paginator = Paginator(all_todos, items_per_page)
    page = request.GET.get('page')

    try:
        all_todos = paginator.page(page)
    except PageNotAnInteger:
        all_todos = paginator.page(1)
    except EmptyPage:
        all_todos = paginator.page(paginator.num_pages)

    return render(request, 'todos/todos.html',
                  {'all_todos': all_todos, 'title_filter': title_filter, 'due_date_filter': due_date_filter,
                   'items_per_page': items_per_page})

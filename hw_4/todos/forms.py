from django import forms
from .models import TodoList, Todo


class CreateTodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter todo list title'}),
            'description': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter todo list description'}),
        }

    auto_id = False


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status', 'todo_list']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Todo title'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Todo description'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter due date'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'todo_list': forms.Select(attrs={'class': 'form-select'}),
        }

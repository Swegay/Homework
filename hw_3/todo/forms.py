from django import forms


class CreateTodoForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=255, required=True)
    description = forms.CharField(min_length=0, max_length=1000, required=False)
    due_date = forms.DateTimeField()
    status = forms.BooleanField(required=False)

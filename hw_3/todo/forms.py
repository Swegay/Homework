from django import forms


class CreateTodoForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=255, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Enter your to do title'
                                                          }))
    description = forms.CharField(min_length=0, max_length=1000, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Enter description'
                                                                }))
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}, format='%Y-%m-%dT%H:%M'),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

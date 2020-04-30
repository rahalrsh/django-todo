from django import forms
from .models import TodoItem


class TodoCreateForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'placeholder': 'Add a note to your task',
            'rows': '3',
        }
    ))

    class Meta:
        model = TodoItem
        fields = [
            'title',
            'description',
            'done',
        ]



from django import forms
from .models import Task

class TasForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'due_date']
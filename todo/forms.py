from django import forms
from django.forms import ModelForm
from todo.models import Task



class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new Task', 'size':'40'}))

    class Meta:
        model = Task
        fields = '__all__'

    
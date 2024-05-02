from django import forms
from django.forms import ModelForm
from list.models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['complete']
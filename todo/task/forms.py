from django import forms
from django.forms import ModelForm
from .models import *

# Edit: line 8  has been included later to add placeholder for the input Field

class TaskForm(forms.ModelForm): 
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = Tasks
        fields = '__all__'
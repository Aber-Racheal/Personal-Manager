from django import forms
from . import models

# Create your models here.

class CreateTask(forms.ModelForm):
   class Meta:
       models = models.Task
       fields = ['task_title' ,'task_description', 'task_image', 'task_status' ,'task_deadline' ]
       widgets = {
            'task_title': forms.Textarea(attrs={'placeholder':"Enter a title..."}),
            'task_description': forms.Textarea(attrs={'rows': 5, 'cols': 40, 'placeholder': 'Enter task description...'}),
            'task_deadline': forms.DateInput(attrs={'type': 'date'}),
        }
    
    

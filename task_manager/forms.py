from django import forms
#forms is a module from django that helps us work with forms in our applications
from .models import Task
#on the line above, we are importing the task object that we defined in our models.py file

class CreateTask(forms.ModelForm):
   class Meta:
       #class Meta means we are defining meta data for our form
       model = Task
       fields = ['task_title' ,'task_description', 'task_image','task_deadline']
       
       #widgets help us further define what our form will look like and also add extra attributes like placeholders etc.
       widgets = {
            'task_title': forms.Textarea(attrs={'placeholder':"Enter a title..."}),
            'task_description': forms.Textarea(attrs={'rows': 5, 'cols': 40, 'placeholder': 'Enter task description...'}),
            'task_deadline': forms.DateInput(attrs={'type': 'date'}),
        }
    
    

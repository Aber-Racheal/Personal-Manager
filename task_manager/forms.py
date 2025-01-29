from django import forms

# Create your models here.

class TaskForm(forms.Form):
    task_title = forms.CharField(label="Enter task title", max_length= 200, unique=True, blank=False )
    task_description = forms.TextField(label="Enter task desription",blank=False, widget=forms.Textarea)
    task_image = forms.ImageField(blank=True, null=True, default="placeholder.jpg")
    task_status = forms.CharField(
        blank=False,
        default="pending",
        choices = [("pending", "Pending"), ("complete", "Complete")]
    )
    created_time = forms.DateTimeField(auto_now_add=True, blank=False)
    deleted_time = forms.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_time = forms.DateTimeField(auto_now=True)
    task_deadline = forms.DateField(null=True, blank=True,)
    def __str__(self):
        return self.task_title
    
    

from django.db import models

# Create your models here.

class Task(models.Model):
    task_title = models.CharField(max_length= 200, unique=True, blank=False )
    task_description = models.TextField(blank=False)
    task_image = models.ImageField(blank=True, null=True)
    task_status = models.CharField(
        blank=False,
        default="pending",
       status_choices = [("pending", "Pending"), ("complete", "Complete")]
    )
    created_time = models.DateTimeField(auto_now_add=True)
    deleted_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    

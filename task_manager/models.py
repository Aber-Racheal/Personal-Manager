from django.db import models

# Create your models here.

class Task(models.Model):
    task_title = models.CharField(max_length= 200, unique=True, blank=False )
    task_description = models.TextField(blank=False)
    task_image = models.ImageField(blank=True, null=True, default="placeholder.jpg")
    task_status = models.CharField(
        max_length= 50,
        blank=False,
        default="pending",
        choices = [("pending", "Pending"), ("complete", "Complete")]
    )
    created_time = models.DateTimeField(auto_now_add=True, blank=False)
    deleted_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_time = models.DateTimeField(auto_now=True)
    task_deadline = models.DateField(null=True, blank=True,)
    def __str__(self):
        return self.task_title
    
    

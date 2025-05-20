from django.db import models

#the models.py file helps us define the structure and attributes of our table in the database
#In this case, the table is called Task in our database

#In this tabe, the columns are as listed: task_title, description,image,status, created time,etc..
class Task(models.Model):
    task_title = models.CharField(max_length= 200, unique=True, blank=False )
    task_description = models.TextField(blank=False)
    task_image = models.ImageField(blank=True, null=True, default="placeholder.jpg")
    task_status = models.CharField(
        max_length= 50,
        blank=False,
        default="pending",
        choices = [("pending", "Pending"), ("complete", "Complete"), ("overdue", "Overdue"), ]
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    deleted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_deadline = models.DateTimeField(null=True, blank=True,)
    is_in_trash = models.BooleanField(default=False) 
    def __str__(self):
        return self.task_title
    
    

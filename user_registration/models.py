from django.db import models

# Create your models here.
class User(models.Model):
    # user_id = models
    full_name = models.CharField(max_length = 255, unique="true", null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(unique = True, max_length=25, blank= False, null = False)
    
    def __str__(self):
        return self.full_name
    
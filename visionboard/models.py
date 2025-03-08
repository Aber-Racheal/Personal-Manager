from django.db import models

# Create your models here.
class VisionBoard(models.Model):
    vision_name = models.CharField(max_length=200, null=False, blank=False)
    vision_year= models.DateTimeField(null=False, blank=False, auto_now_add=True)
    vision_image= models.ImageField(null=False, blank=False, default='placeholder.png')
    vision_quote= models.TextField(null=True, blank=True)
    is_in_trash = models.BooleanField(default=False)  
    def __str__(self):
        return self.vision_name  
    
     
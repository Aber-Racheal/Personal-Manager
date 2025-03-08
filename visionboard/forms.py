from .models import VisionBoard
from django import forms

class VisionForm(forms.ModelForm):
    
    class Meta:
        model = VisionBoard
        fields = ("vision_name", "vision_image", "vision_quote",)
        
        

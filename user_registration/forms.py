from django import forms
from .models import User


class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'full_name', 'email', 'password'
        ]
        widgets = {
            'full_name':forms.Textarea(attrs={'placeholder':"Enter Full Name"})
        }
        
from django import forms 
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class tectstackforms(forms.ModelForm):
    class Meta:
        model=techstack
        fields="__all__"

class registrationpage(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

class loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
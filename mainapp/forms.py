from django import forms 
from . models import *
class tectstackforms(forms.ModelForm):
    class Meta:
        model=techstack
        fields="__all__"
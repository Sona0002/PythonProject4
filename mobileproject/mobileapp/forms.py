from django import forms
from . models import Mobile

class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobile
        fields=['model_name','price','desc','img']

from django import forms
from .models import *

class remainder_form(forms.ModelForm):
    class  Meta:
        model = remainder
        fields = '__all__'
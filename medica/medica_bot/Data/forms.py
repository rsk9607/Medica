from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Patient

class medica_form(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['user','full_name']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'format': 'dd-mm-yyyy'}),
        }
        
        
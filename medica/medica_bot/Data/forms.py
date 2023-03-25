from django import forms
from .models import Patient

class medica_form(forms.ModelForm):
    class Meta:
        model = Patient
        feild ="__all__"
        
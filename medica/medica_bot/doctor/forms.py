from django import forms
from .models import doctor

class medica_doctor(forms.ModelForm):
    class Meta:
        model = doctor
        feild = '__all__'

 
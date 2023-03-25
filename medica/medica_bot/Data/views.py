from django.http import HttpResponse
from django.template import loader
from .models import Patient
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required

@login_required
def register_medica(request):
    context ={}
    template = loader.get_template('register_medica.html')
    return HttpResponse(template.render(context, request))

def profile(request):
    patient = Patient.objects.all().values()
    template = loader.get_template('profile.html')
    context ={
    'mypatient':patient
    }
    return HttpResponse(template.render(context, request))



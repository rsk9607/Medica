from django.http import HttpResponse
from django.template import loader
from .models import Patient

def profile(request):
    patient = Patient.objects.all().values()
    template = loader.get_template('profile.html')
    context ={
    'mypatient':patient
    }
    return HttpResponse(template.render(context, request))
    

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Patient
from django.shortcuts import redirect,render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def register_medica(request):
    researcher = ''
    study = ''
    context ={}
    if request.method == "POST":
        user = request.user
        full_name = request.user.first_name +''+ request.user.last_name
        date_0f_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        emergency_contact_name = request.POST.get('emergency_contact_name')
        emergency_contact_phone = request.POST.get('emergency_contact_phone')
        medical_history = request.POST.get('medical_history')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        physician_notes = request.POST.get('physician_notes')
        
        data = Patient.objects.create(user=user,full_name=full_name,date_of_birth=date_0f_birth,address=address,gender=gender,phone_number=phone_number,emergency_contact_name=emergency_contact_name,emergency_contact_phone=emergency_contact_phone,medical_history =medical_history,height=height,weight=weight,physician_notes=physician_notes)

        data.save()
        return redirect('/home')
    else:    
        template = loader.get_template('register_medica.html')
        return HttpResponse(template.render(context, request))
    
def edit(request):
    researcher = ''
    study = ''
    user = request.user
    patient = Patient.objects.get(user=user)
    context ={
        'patient':patient,
    }
    if request.method == "POST":
        patient.full_name = request.POST.get('full_name')
        # patient.date_of_birth = request.POST.get('date_of_birth')
        patient.address = request.POST.get('address')
        patient.gender = request.POST.get('gender')
        patient.phone_number = request.POST.get('phone_number')
        patient.emergency_contact_name = request.POST.get('emergency_contact_name')
        patient.emergency_contact_phone = request.POST.get('emergency_contact_phone')
        patient.medical_history = request.POST.get('medical_history')
        patient.height = request.POST.get('height')
        patient.weight = request.POST.get('weight')
        patient.physician_notes = request.POST.get('physician_notes')
        patient.save()
        return redirect('/profile')
    else:    
        template = loader.get_template('edit.html')
        return HttpResponse(template.render(context, request))

def profile(request):
    patient = Patient.objects.all().values()
    template = loader.get_template('profile.html')
    context ={
    'mypatient':patient
    }
    return HttpResponse(template.render(context, request))



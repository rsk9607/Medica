from django.http import HttpResponse
from django.template import loader
from .models import Doctor,Appointment
from Data.models import Patient
from django.shortcuts import redirect,render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def medica_doctor(request):
  context = {}
  if request.method == 'POST':
    user = request.user
    name = request.user.first_name +' '+ request.user.last_name
    specialty = request.POST.get('specialty')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    email = request.user.email
    bio = request.POST.get('bio')
    
    Doctor.objects.create(user=user,name=name,specialty=specialty,address=address,phone=phone,email=email,bio=bio).save()
    return redirect('/home')
  else:    
        template = loader.get_template('doc_reg.html')
        return HttpResponse(template.render(context, request))  

def appointment(request):
  doctor = Doctor.objects.all()
  try:
    patient = Patient.objects.get(user=request.user)
  except:
    return redirect('/login/')
  if request.method == 'POST':
    doctor_id=  request.POST.get('book')
    patient_name = patient.full_name
    patient_email = patient.user.email
    past_history = patient.medical_history
    Physician_Note = patient.physician_notes
    Appointment.objects.create(doctor_id=doctor_id,patient_name=patient_name,patient_email=patient_email,past_history=past_history,Physician_Note=Physician_Note).save()
    return redirect('concern')
  else:
    context = {
    'doctor':doctor,
    }
    template = loader.get_template('appointment.html')
    return HttpResponse(template.render(context,request))

def concern(request):
  patient = Patient.objects.get(user=request.user)
  appointment = Appointment.objects.get(appointment_date__isnull=True)
  context ={}
  if request.method == "POST":
    appointment.appointment_date = request.POST.get('appointment_date')
    appointment.appointment_reason = request.POST.get('appointment_reason')
    appointment.save()
    return redirect('profile')
  else:
    template = loader.get_template('concern.html')
    return HttpResponse(template.render(context,request))

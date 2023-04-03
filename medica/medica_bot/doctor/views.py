from django.http import HttpResponse
from django.template import loader
from .models import Doctor
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
  template = loader.get_template('appointment.html')
  doctor = Doctor.objects.all().values()
  context = {
    'doctor':doctor,
  }
  return HttpResponse(template.render(context,request))

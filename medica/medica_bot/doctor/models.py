from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True)
    specialty = models.CharField(max_length=255)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    bio = models.TextField(blank=True)

def __str__(self):
    return self.name
 
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255)
    patient_email = models.EmailField()
    appointment_date = models.DateTimeField()
    appointment_reason = models.TextField()
    
def __str__(self):
        return self.patient_name + " - " + str(self.appointment_date)

    


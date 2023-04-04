from django.contrib import admin
from .models import Doctor,Appointment

class doctormodelAdmin(admin.ModelAdmin):
    list_display = ('user','name','specialty','phone','email')

class AppointmentmodelAdmin(admin.ModelAdmin):
    list_display = ('patient_name','appointment_date')

admin.site.register(Doctor,doctormodelAdmin)
admin.site.register(Appointment,AppointmentmodelAdmin)


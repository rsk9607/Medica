from django.contrib import admin
from .models import Patient

class patientmodelAdmin(admin.ModelAdmin):
    list_display =('user','full_name','date_of_birth', 'phone_number')

admin.site.register(Patient,patientmodelAdmin)
# Register your models here.

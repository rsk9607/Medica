from django.contrib import admin
from .models import Doctor

class doctormodelAdmin(admin.ModelAdmin):
    list_display = ('user','name','specialty','phone','email')

admin.site.register(Doctor,doctormodelAdmin)

from django.contrib import admin
from .models import *

class RemainderAdmin(admin.ModelAdmin):
    list_display = ("name","description","number_time","time_gap")

admin.site.register(remainder,RemainderAdmin)
# Register your models here.

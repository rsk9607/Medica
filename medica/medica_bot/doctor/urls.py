from django.urls import path
from . import views

urlpatterns = [
   path('appointment/',views.appointment, name='appointment'),
   path('medica_doctor/',views.medica_doctor, name='medica_doctor'),
   path('concern/',views.concern, name='concern'),
   path('list/',views.list, name='listed appointment' )
]
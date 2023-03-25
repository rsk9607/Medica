from django.contrib import admin
from django.urls import path
from . import views
from .views import chatbot



urlpatterns = [
    path('chatbot/',views.chatbot,name='chatbot')
]
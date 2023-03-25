from django.urls import path
from . import views
from Bot.views import chatbot

urlpatterns = [
    path('', views.home, name='home'),
]
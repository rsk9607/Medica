from django.urls import path
from . import views

urlpatterns = [
    path('remainder/', views.remainders, name='remainder'),
]
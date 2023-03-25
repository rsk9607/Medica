from django.urls import path
from . import views

urlpatterns = [
    path('pharmacy/', views.EP_home, name='pharmacy')
]

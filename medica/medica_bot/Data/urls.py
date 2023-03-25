from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('register_medica/', views.register_medica, name="register_medica")
]

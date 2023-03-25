from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('register/login',views.login_user,name='register'),
]

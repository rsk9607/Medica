from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password,check_password

def login_user(request):
  researcher = ''
  study = ''
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      template = loader.get_template('index.html')
      return HttpResponse(template.render())
    else:
      messages.error(request,("There was an error logging in. TRY AGAIN!"))
      template = loader.get_template('login.html')
      return HttpResponse(template.render())
  else:
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def logout_user(request):
  logout(request)
  messages.success(request,("You Are Logged Out!"))
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def register_user(request):
  researcher = ''
  study = ''
  if request.method=="POST":
      first_name=request.POST.get('first_name')
      last_name=request.POST.get('last_name')
      username = request.POST.get('user_name')
      email = request.POST.get('emailid')
      pass1 = request.POST.get('password')
      pass2 = request.POST.get('password2')
      
      if len(username)>10:
          messages.warning(request, "Username must be under 10 characters")
          return redirect('login.html')
      
      if not username.isalnum():
          messages.warning(request, "Username can only contain Letters and Numbers")
          return redirect('login.html')
      
      if pass1 != pass2:
          messages.warning(request, "Passwords do not match")
          return redirect('login.html')
      
      user = User.objects.create(username=username,email=email,password=make_password(pass1),first_name=first_name,last_name=last_name)
      user.save()
      messages.success(request, " Your CinemaShow account has been succesfully created ")
      return redirect(login)
  else:
    template = loader.get_template('register.html')
    return HttpResponse(template.render())
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import remainder_form

def remainders(request):
  myremainder = remainder.objects.all().values()
  template = loader.get_template('remainder.html')
  context ={
    'myremainder':myremainder
  }
  form = remainder_form()
  if request.method == 'POST':
    print(request.POST)
    form = remainder_form(request.POST)
    if form.is_valid():
      form.save()
  form = remainder_form()  
  context['form'] = form
  return HttpResponse(template.render(context, request))

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def EP_home(request):
    template = loader.get_template('EP_Home.html')
    return HttpResponse(template.render())

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def EP_home(request):
    context ={}
    template = loader.get_template('EP_Home.html')
    return HttpResponse(template.render(context,request))

# Create your views here.

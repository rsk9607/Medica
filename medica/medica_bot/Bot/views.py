from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_KEY",None)
openai.api_key=api_key
def chatbot(request):
    chatbot_response=None
    if api_key is not None and request.method == "POST":
        user_input=request.POST.get('user_input')
        prompt=user_input

        response=openai.Completion.create(
            engine = 'text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            temperature=0.5
        )

        print(response)
        chatbot_response=response["choices"][0]['text']
    return render(request,'bot_index.html',{"response":chatbot_response})

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

# Create your views here.

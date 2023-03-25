from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.contrib.auth.models import User
import openai, os
from dotenv import load_dotenv
from Data.models import Patient
load_dotenv()

api_key = os.getenv("OPENAI_KEY",None)
openai.api_key=api_key
chatbot_response=None
def chatbot(request):
    chatbot_response=None
    if api_key is not None and request.method == "POST":
        user_input=request.POST.get('user_input')
        prompt=user_input
        history= 'hi'
        prompt = f"If the question is related to health,disease,personal hygiene,suggestions for health-answer this-patient history-{history} : {user_input},else say: I am only made to answer to health related queries.Thank You!"
        response=openai.Completion.create(
            engine = 'text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            temperature=0.5
        )
        print(response)
        chatbot_response=response["choices"][0]['text']
        chatbot_web()
    return render(request,'bot_index.html',{"response":chatbot_response})

def chatbot_web():
   return JsonResponse({'response':chatbot_response})


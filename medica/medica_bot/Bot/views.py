from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.contrib.auth.models import User
import openai, os
from dotenv import load_dotenv
from Data.models import Patient
from django.shortcuts import redirect,render
load_dotenv()

api_key = os.getenv("OPENAI_KEY",None)
openai.api_key=api_key
# @login_required
def chatbot(request):
    try:
        patient = Patient.objects.get(user=request.user)
    except:
        return redirect('/login/')
    chatbot_response=None
    if api_key is not None and request.method == "POST":
        user_input=request.POST.get('user_input')
        # prompt=user_input
        user = request.user
        patient = Patient.objects.get(user=user)
        context ={
        'patient':patient,
        }
        history=patient.medical_history
        physician=patient.physician_notes
        # username=request.user
        # hist=Patient.objects
        # history= Patient.objects.get(user=username).values_list('medical_history',flat=True)
        prompt = f"patient's medical history is this -{history} and the physician response on the medical history is this- {physician} : {user_input}"
        response=openai.Completion.create(
            engine = 'text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            temperature=0.5
        )
        print(response)
        chatbot_response=response["choices"][0]['text']
        # chatbot_web()
        brief=f"{chatbot_response}----draw conclusions from this in no more than 50 words"
        response=openai.Completion.create(
            engine = 'text-davinci-003',
            prompt=brief,
            max_tokens=256,
            temperature=0.5
        )
        chatbot_response2=response["choices"][0]['text']
        patient.medical_history=history+"question: "+user_input+" response: "+chatbot_response2
        patient.save()

    return render(request,'bot_index.html',{"response":chatbot_response})

# def chatbot_web():
#    return JsonResponse({'response':chatbot_response})


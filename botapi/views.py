from django.shortcuts import render
import requests
from django.http import HttpResponse

def index(request):
    output = "welCome to Our SiTE"
    return HttpResponse(output)

def home(request):
    response = requests.get('https://freegeoip.app/json/')#http://freegeoip.net/
    geodata = response.json()
    return HttpResponse("Your ip-address is %s and country name %s." % (geodata['ip'] , geodata['country_name']) )
'''
def home(request):
    response = requests.get('https://freegeoip.app/json/')#http://freegeoip.net/
    geodata = response.json()
    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })
'''
def detail(request, question):
    return HttpResponse("We got your query :: %s." % question)

def answer(request):
    question_id = 1456
    return HttpResponse("You're looking at answer for Q No %s." % question_id)

import botapi.chitChat as cc
from .models import Chat
def chat(request):
    chat_obj = Chat()
    q = request.GET.get("question")
    chat_obj = cc.chatbot_response(q)
    #a = "ans is %s" %(q)
    print("111111111111111111111111111")
    print(chat_obj)
    print("5555555555")
    return HttpResponse(chat_obj.a)

'''
#working one
def chat(request):
    q = request.GET.get("question")
    a = "ans is %s" %(q)
    return HttpResponse(a)
'''
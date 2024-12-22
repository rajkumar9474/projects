from django.shortcuts import render
from django.http import HttpResponse,HttpResponsePermanentRedirect

# Create your views here.
def home(request):
    return HttpResponsePermanentRedirect('/index/')


def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def donate_blood(request):
    return render(request,'blood_donate.html')

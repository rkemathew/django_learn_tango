from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango Says: Hello World!<br/>Here is the <a href='./about'>about</a> page.")

def about(request):
    return HttpResponse("Rango Says: Here is the about page.<br/>Click <a href='/rango'>here</a> to go back.")

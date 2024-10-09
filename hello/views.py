from django.http import HttpResponse                #Importing HttpResponse from django.http
from django.shortcuts import render

# Create your views here.

def index(request):                                 #Defining a function index which takes request as an argument
    return HttpResponse("Hello, world!")            #Returning a HttpResponse with "Hello, world!" as content

def rahul(request):
    return HttpResponse("Hello, Rahul!")

def shyam(request):
    return HttpResponse("Hello, Shyam!")

def suraj(request):
    return HttpResponse("Hello, Suraj!")

def rishi(request):
    return HttpResponse("Hello Rishi")

def kartik(request):
    return HttpResponse("Hello, Kartik!")

def aryan(request):
    return HttpResponse("Hello, Aryan!")

def raghu(request):
    return HttpResponse("Hello, Raghu!")

def rohan(request):
    return HttpResponse("Hello, Rohan!")

def suresh(request):
    return HttpResponse("Hello, Suresh!")

def ramesh(request):
    return HttpResponse("Hello, Ramesh!")

def rajesh(request):
    return HttpResponse("Hello, Rajesh")

def ravi(request):
    return HttpResponse("Hello, Ravi!")

def rohit(request):
    return HttpResponse("Hello, Rohit!")

def sumit(request):
    return HttpResponse("Hello, Sumit!")

def sarthak(request):
    return HttpResponse("Hello, Sarthak!")
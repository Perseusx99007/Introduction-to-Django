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
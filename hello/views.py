from django.http import HttpResponse                #Importing HttpResponse from django.http
from django.shortcuts import render

# Create your views here.

def index(request):                                 #Defining a function index which takes request as an argument
    return HttpResponse("Hello, world!")            #Returning a HttpResponse with "Hello, world!" as content

def perseus(request):
    return HttpResponse("Hello, Perseus!")

def lucifer(request):
    return HttpResponse("Hello, Lucifer!")

def orion(request):
    return HttpResponse("Hello, Orion!")
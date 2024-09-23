from django.http import HttpResponse                #Importing HttpResponse from django.http
from django.shortcuts import render

# Create your views here.

def index(request):                                 #Defining a function index which takes request as argument
    return HttpResponse("Hello, world!")            #Returning a HttpResponse with "Hello, world!" as content

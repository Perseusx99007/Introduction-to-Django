#Creating a urls.py file for the Django app (Hello)

from django.urls import path                    #Importing path from django.urls

from . import views                             #Importing views from the current directory

#Defining the url pattern for the index view. When the root / default URL is requested, the index view will be called. The name parameter is used to refer to this URL pattern in other parts of the application. Here "views" refers to the views.py file in the same directory and "index" refers to the index function in that file.

urlpatterns = [
    path("", views.index, name='index'),
    path("rahul", views.rahul, name='rahul'),
    path("shyam", views.shyam, name='shyam'),
    path("suraj", views.suraj, name='suraj'),
    path("rishi", views.rishi, name='rishi'),
    path("kartik", views.kartik, name='kartik'),
    path("aryan", views.aryan, name='aryan'),
    path("raghu", views.raghu, name='raghu'),
    path("rohan", views.rohan, name='rohan'),
    path("suresh", views.suresh, name='suresh'),
    path("ramesh", views.ramesh, name= 'ramesh'),
    path("rajesh", views.rajesh, name='rajesh'),
    path("ravi", views.ravi, name='ravi'),
    path("rohit", views.rohit, name='rohit'),
    path("sumit", views.sumit, name='sumit'),
    path("sarthak", views.sarthak, name='sarthak'),
    path("amit", views.amit, name='amit'),
    path("akshay", views.akshay, name='akshay'),
    path("aniket", views.aniket, name='aniket'),
    path("abhay", views.abhay, name='abhay'),
    path("anil", views.anil, name='anil'),
    path("abhay", views.abhay, name='abhay'),
    path("vivek", views.vivek, name='vivek'),
    path("vikram", views.vikram, name='vikram'),
    path("aditya", views.aditya, name='aditya'),
    path("ankit", views.ankit, name='ankit'),
    path("anuj", views.anuj, name='anuj'),
    path("anmol", views.anmol, name='anmol'),
    path("ajay", views.ajay, name='ajay'),
    path("anand", views.anand, name='anand'),
    path("anirudh", views.anirudh, name='anirudh'),
    path("arjun", views.arjun, name='arjun'),
    path("arun", views.arun, name='arun'),
    path("ashish", views.ashish, name='ashish'),
]
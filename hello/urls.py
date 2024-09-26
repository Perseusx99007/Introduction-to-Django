#Creating a urls.py file for the Django app (Hello)

from django.urls import path                    #Importing path from django.urls

from . import views                             #Importing views from the current directory

#Defining the url pattern for the index view. When the root / default URL is requested, the index view will be called. The name parameter is used to refer to this URL pattern in other parts of the application. Here "views" refers to the views.py file in the same directory and "index" refers to the index function in that file.

urlpatterns = [
    path("", views.index, name='index'),
    path("perseus", views.perseus, name='perseus'),
    path("lucifer", views.lucifer, name='lucifer'),
    path("orion", views.orion, name='orion'),
]
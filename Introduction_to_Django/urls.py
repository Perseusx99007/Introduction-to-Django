"""
URL configuration for Introduction_to_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path                         #Importing include and path from django.urls

# Adding a URL to urlpatterns:  path('hello/', include("hello.urls")) i.e. when the URL is 'hello/' then include the urls from the hello app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls")),                    
]

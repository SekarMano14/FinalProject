"""
URL configuration for MyFirstDjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from RegisterPage import views as v1
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('empdetails/',v1.retrive_employee),
    path('addemp/',v1.addnew_employee),
    path('deleteemp/<id>',v1.delete_employee),
    path('updateemp/<id>',v1.update_employee),


]

import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from RegisterPage.models import Employee

from RegisterPage.forms import EmployeeForm


def retrive_employee(request):
    emp = Employee.objects.all()
    return render(request,"register/employeedetails.html",context={"emp":emp})



def addnew_employee(request):
    form=EmployeeForm()
    if request.method=="POST":
      form= EmployeeForm(request.POST)
      if form.is_valid():
          form.save()
          return HttpResponse("<h1>Successfully Registered <a href='/empdetails'>Clike here to employeedetails</a></h1>")
    return render(request,"register/addemployee.html",context={"form":form})


def delete_employee(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return HttpResponse("<h1>User data Delete Successfully <a href='/empdetails'>Clike here</a> to View the Updated employeedetails</h1>")

def update_employee(request,id):
    emp = Employee.objects.get(id=id)
    if request.method=="POST":
        form = EmployeeForm(request.POST,instance=emp)
        if form.is_valid:
            form.save()
            return HttpResponse("<h1>Update data Successfully<a href='/empdetails'>Clike here</a> to View the Updated employeedetails</h1>")
    return render(request,"register/updateform.html",context={"emp":emp})


from django.shortcuts import render,HttpResponse
from .models import Employee

# Create your views here.
def display(request,Name):
    emp=Employee.objects.filter(Name=Name)
    context={"emp":emp}
    return render(request,"index.html",context)


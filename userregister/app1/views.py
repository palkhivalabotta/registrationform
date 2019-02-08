from django.shortcuts import render
from .models import employee



def RegisterUser(request):
    name = request.POST.get('NAME')
    age = request.POST.get('AGE')
    salary = request.POST.get('SALARY')
    u=employee(name=name,age=age,salary=salary).save()
    return render(request,"loginform.html",{"message":"User Registered"})

def userregister(request):
    return render(request,"registrationform.html")
def openhomepage(request):
    return render(request, "loginform.html")
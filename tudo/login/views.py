from django.shortcuts import render

# Create your views here.


def login(request):
    print("login page is called! ")
    return render(request,"login.html",{})


def register(request):
    print("Register page is called! ")
    return render(request,"register.html",{})



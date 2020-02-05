from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import *
from django.contrib.auth import authenticate, login, get_user_model
def index(request):
    context = {
        'form': hello
    }
    return render(request,"hello.html",context)

def login(request):
    form = Login(request.POST or None)
    context = {
        'form' : Login
    }
    return render(request,"login.html",context)
User = get_user_model()
def reg(request):
    form = Register(request.POST or None)
    context = {
        'form' : Register
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_User = User.objects.create_user(username,email,password)
    return render(request,"regist.html",context)

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth

# Create your views here.

def login(request):
    return render(request, 'studentapp/login.html')

def authen(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/studentapp/index/")
    else:
        return HttpResponse("<h1>No such user</h1>")

def index(request):
    return render(request, 'studentapp/index.html')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'studentapp/login.html')

def index(request):
    username = request.POST['username']
    password = request.POST['password']
    username = str(username)
    password = str(password)
    return HttpResponse("<h1>Username: "+username+" Password: "+password+"</h1>")
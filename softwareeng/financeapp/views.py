from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('financeapp:login'))
    return HttpResponse("You should not see this")

def login(request):
    return render(request, 'financeapp/login.html')

def logincheck(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return render(request, 'financeapp/login.html', {
            'error_message': "Username or password is incorrect"
        })
    else:
        return render(request, 'index.html')

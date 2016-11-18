from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    pw = request.user.password
    return render(request, 'financeapp/index.html', {'pw': pw})

def loginview(request):
    return render(request, 'financeapp/login.html', {'next': request.GET['next']})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse("financeapp:login"))

def logincheck(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return render(request, 'financeapp/login.html', {
            'error_message': "Username or password is incorrect"
        })
    else:
        login(request, user)
        next_page = request.POST['next']
        if next_page:
            return HttpResponseRedirect(next_page)
        else:
            return HttpResponseRedirect(reverse("financeapp:index"))

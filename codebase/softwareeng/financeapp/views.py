import decimal
from financeapp.accountgetter import AccountGetter
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from financeapp.models import Account, StudentAccount

@login_required
def student(request, student_id):
    account_getter = AccountGetter(request.user)
    student_account = account_getter.student_account
    if student_account.get_pk() != int(student_id):
        return HttpResponseForbidden()
    context = {'full_name': account_getter.account.full_name}
    return render(request, 'financeapp/student.html', context)

@login_required
def checkbalanceview(request, student_id):
    student_account = AccountGetter(request.user).student_account
    context = {'funds': student_account.get_funds()}
    return render(request, 'financeapp/check_balance.html', context)

@login_required
def addmoneyview(request, student_id):
    student_account = AccountGetter(request.user).student_account
    context = {'funds': student_account.get_funds(), 'student_id': student_id}
    return render(request, 'financeapp/add_money.html', context)

@login_required
def doaddmoney(request, student_id):
    account_getter = AccountGetter(request.user)
    student_account = account_getter.student_account
    amount = decimal.Decimal(request.POST["amount"])
    student_account.deposit(amount)
    kwargs = {'student_id': student_id}
    return HttpResponseRedirect(reverse("financeapp:add_money", kwargs=kwargs))

def loginview(request):
    if 'next' in request.GET:
        return render(request, 'financeapp/login.html', {'next': request.GET['next']})
    else:
        return render(request, 'financeapp/login.html')

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
        account_getter = AccountGetter(user)
        student_account = account_getter.student_account
        student_id = student_account.get_pk()
        if 'next' in request.POST and request.POST['next'] != "":
            return HttpResponseRedirect(request.POST['next'])
        else:
            kwargs = {'student_id': student_id}
            return HttpResponseRedirect(reverse("financeapp:student", kwargs=kwargs))
        

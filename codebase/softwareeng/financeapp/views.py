import decimal
from financeapp.accountgetter import AccountGetter
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.contrib.auth.decorators import login_required
from financeapp.models import Account, StudentAccount
from financeapp.permissionchecker import PermissionChecker

@login_required
def student(request, student_id):
    account_getter = AccountGetter(request.user)
    if not PermissionChecker.check_permissions(account_getter, student_id):
        return HttpResponseForbidden()
    context = {'full_name': account_getter.account.full_name}
    return render(request, 'financeapp/student.html', context)

@login_required
def parenthome(request):
    account_getter = AccountGetter(request.user)
    if not account_getter.parent_account:
        return HttpResponseForbidden()
    children = account_getter.parent_account.get_children()
    for i in range(len(children)):
        children[i] = {
            'full_name': children[i].get_full_name(),
            'pk': children[i].get_pk()
        }
    context = {
        'full_name': account_getter.parent_account.get_full_name(),
        'children': children
    }
    return render(request, 'financeapp/parenthome.html', context)

@login_required
def checkbalanceview(request, student_id):
    account_getter = AccountGetter(request.user)
    if not PermissionChecker.check_permissions(account_getter, student_id):
        return HttpResponseForbidden()
    if account_getter.student_account:
        student_account = account_getter.student_account
    else:
        student_account = account_getter.parent_account.get_child(student_id)
    context = {'funds': student_account.get_funds()}
    return render(request, 'financeapp/check_balance.html', context)

@login_required
def addmoneyview(request, student_id):
    account_getter = AccountGetter(request.user)
    if not PermissionChecker.check_permissions(account_getter, student_id):
        return HttpResponseForbidden()
    if account_getter.student_account:
        student_account = account_getter.student_account
    else:
        student_account = account_getter.parent_account.get_child(student_id)
    context = {'funds': student_account.get_funds(), 'student_id': student_id}
    return render(request, 'financeapp/add_money.html', context)

@login_required
def doaddmoney(request, student_id):
    account_getter = AccountGetter(request.user)
    if not PermissionChecker.check_permissions(account_getter, student_id):
        return HttpResponseForbidden()
    if account_getter.student_account:
        student_account = account_getter.student_account
    else:
        student_account = account_getter.parent_account.get_child(student_id)
    amount = decimal.Decimal(request.POST["amount"])
    student_account.deposit(amount)
    kwargs = {'student_id': student_id}
    return HttpResponseRedirect(reverse("financeapp:add_money", kwargs=kwargs))

@login_required
def loginredir(request):
    account_getter = AccountGetter(request.user)

    if account_getter.student_account:
        student_account = account_getter.student_account
        student_id = student_account.get_pk()
        if 'next' in request.POST and request.POST['next'] != "":
            return HttpResponseRedirect(request.POST['next'])
        else:
            kwargs = {'student_id': student_id}
            return HttpResponseRedirect(reverse("financeapp:student", kwargs=kwargs))
    else:
        return HttpResponseRedirect(reverse("financeapp:parenthome"))

# Password reset views
def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='registration/password_reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('financeapp:login'))


def reset(request):
    return password_reset(request, template_name='registration/password_reset.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        post_reset_redirect=reverse('financeapp:login'))

import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

#Fix this later to get account dynamically
def get_null_account():
    #User = get_user_model()
    #null_user = User.objects.get(username='null_user')
    #null_account = Account.objects.get(user=null_user)
    #return null_account.pk
    return 3

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    ACCOUNT_TYPES = (
        ('P', 'Parent'),
        ('S', 'Student')
    )
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPES)
    def change_password(self, new_password):
        return self.user.set_password(new_password)

class StudentAccount(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, default=get_null_account())
    funds = models.DecimalField(max_digits=6, decimal_places=2)
    def get_full_name(self):
        return self.account.full_name
    def __str__(self):
        return self.account.full_name
    def deposit(self, amount):
        self.funds += amount
        super(StudentAccount, self).save()
        return True

class ParentAccount(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, default=get_null_account())
    student_accounts = models.ManyToManyField(StudentAccount)
    def get_full_name(self):
        return self.account.full_name
    def __str__(self):
        return self.account.full_name

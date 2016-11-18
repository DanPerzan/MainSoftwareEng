import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    ACCOUNT_TYPES = (
        ('P', 'Parent'),
        ('S', 'Student')
    )
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPES)

class StudentAccount(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    funds = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.full_name
    def deposit(self, amount):
        self.funds += amount
        super(StudentAccount, self).save(*args, **kwargs)
        return true
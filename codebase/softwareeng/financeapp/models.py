import datetime
from django.db import models
from django.utils import timezone

class StudentAccount(models.Model):
    #the django user associated with the account
    user = models.ForeignKey(User, unique=True)
    #the student's full name
    full_name = models.char_field(max_length=100)
    #money in the account
    funds = models.DecimalField(max_digits=6, decimal_place=2)
    def __str__(self):
        return self.full_name
    def deposit(self, amount):
        return true
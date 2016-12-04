from django.test import TestCase
from django.contrib.auth.models import User
from financeapp.models import Account, StudentAccount, ParentAccount
from financeapp.studentwrapper import StudentWrapper
from financeapp.parentwrapper import ParentWrapper

class StudentTestCase(TestCase):
    def setUp(self):
        suser = User.objects.create_user("testuser", "", "pwpwpw")
        saccount = Account.objects.create(user=suser, account_type="S", full_name="Test User")
        sstudent = StudentAccount.objects.create(account=saccount, funds=100)
        swrapper = StudentWrapper(sstudent)
    
    def test_get_full_name(self):
        suser = User.objects.get(username="testuser")
        saccount = Account.objects.get(user=suser)
        sstudent = StudentAccount.objects.get(account=saccount)
        swrapper = StudentWrapper(sstudent)
        self.assertEqual(swrapper.get_full_name(), "Test User")

    def test_get_account(self):
        suser = User.objects.get(username="testuser")
        saccount = Account.objects.get(user=suser)
        sstudent = StudentAccount.objects.get(account=saccount)
        swrapper = StudentWrapper(sstudent)
        self.assertEqual(swrapper.get_account(), saccount)

    def test_get_funds(self):
        suser = User.objects.get(username="testuser")
        saccount = Account.objects.get(user=suser)
        sstudent = StudentAccount.objects.get(account=saccount)
        swrapper = StudentWrapper(sstudent)
        self.assertEqual(swrapper.get_funds(), 100)
    
    def test_deposit(self):
        suser = User.objects.get(username="testuser")
        saccount = Account.objects.get(user=suser)
        sstudent = StudentAccount.objects.get(account=saccount)
        swrapper = StudentWrapper(sstudent)
        swrapper.deposit(100)
        self.assertEqual(swrapper.get_funds(), 200)
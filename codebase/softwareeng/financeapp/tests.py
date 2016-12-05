from django.test import TestCase
from django.contrib.auth.models import User
from financeapp.models import Account, StudentAccount, ParentAccount
from financeapp.studentwrapper import StudentWrapper
from financeapp.parentwrapper import ParentWrapper
from financeapp.accountgetter import AccountGetter
from financeapp.permissionchecker import PermissionChecker

class StudentTestCase(TestCase):
    def setUp(self):
        suser = User.objects.create_user("teststudent", "", "pwpwpw")
        saccount = Account.objects.create(user=suser, account_type="S", full_name="Test Student")
        sstudent = StudentAccount.objects.create(account=saccount, funds=100)
        swrapper = StudentWrapper(sstudent)

    def get_student_wrapper(self):
        account_getter = AccountGetter(User.objects.get(username="teststudent"))
        return account_getter.student_account
    
    def test_get_full_name(self):
        swrapper = self.get_student_wrapper()
        self.assertEqual(swrapper.get_full_name(), "Test Student")

    def test_get_account(self):
        swrapper = self.get_student_wrapper()
        suser = User.objects.get(username="teststudent")
        saccount = Account.objects.get(user=suser)
        self.assertEqual(swrapper.get_account(), saccount)

    def test_get_funds(self):
        swrapper = self.get_student_wrapper()
        self.assertEqual(swrapper.get_funds(), 100)
    
    def test_deposit(self):
        swrapper = self.get_student_wrapper()
        swrapper.deposit(100)
        self.assertEqual(swrapper.get_funds(), 200)

class ParentTestCase(TestCase):
    def setUp(self):
        suser = User.objects.create_user("teststudent", "", "pwpwpw")
        saccount = Account.objects.create(user=suser, account_type="S", full_name="Test Student")
        sstudent = StudentAccount.objects.create(account=saccount, funds=100)
        swrapper = StudentWrapper(sstudent)
        puser = User.objects.create_user("testparent", "", "pwpwpw")
        paccount = Account.objects.create(user=puser, account_type="P", full_name="Test Parent")
        pparent = ParentAccount.objects.create(account=paccount)
        pparent.save()
        pparent.student_accounts.add(sstudent)
        pparent.save()

    def get_parent_wrapper(self):
        account_getter = AccountGetter(User.objects.get(username="testparent"))
        return account_getter.parent_account
        
    def test_get_full_name(self):
        pwrapper = self.get_parent_wrapper()
        self.assertEqual(pwrapper.get_full_name(), "Test Parent")

    def test_get_account(self):
        puser = User.objects.get(username="testparent")
        paccount = Account.objects.get(user=puser)
        pwrapper = self.get_parent_wrapper()
        self.assertEqual(pwrapper.get_account(), paccount)
    
    def test_get_children(self):
        account_getter = AccountGetter(User.objects.get(username="teststudent"))
        swrapper = account_getter.student_account
        pwrapper = self.get_parent_wrapper()
        self.assertEqual(pwrapper.get_children()[0].get_pk(), swrapper.get_pk())
    
    def test_get_child(self):
        account_getter = AccountGetter(User.objects.get(username="teststudent"))
        swrapper = account_getter.student_account
        pwrapper = self.get_parent_wrapper()
        student_pk = swrapper.get_pk()
        self.assertEqual(pwrapper.get_child(student_pk).get_pk(), student_pk)

class PermissionCheckerTestCase(TestCase):
    def setUp(self):
        cuser = User.objects.create_user("testchild", "", "pw")
        caccount = Account.objects.create(user=cuser, account_type="S")
        cstudent = StudentAccount.objects.create(account=caccount, funds=0)
        cwrapper = StudentWrapper(cstudent)
        ouser = User.objects.create_user("testorphan", "", "pw")
        oaccount = Account.objects.create(user=ouser, account_type="S")
        ostudent = StudentAccount.objects.create(account=oaccount, funds=0)
        owrapper = StudentWrapper(ostudent)
        puser = User.objects.create_user("testparent", "", "pw")
        paccount = Account.objects.create(user=puser, account_type="P")
        pparent = ParentAccount.objects.create(account=paccount)
        pparent.save()
        pparent.student_accounts.add(cstudent)
        pparent.save()

    def test_check_permissions(self):
        child = AccountGetter(User.objects.get(username="testchild"))
        child_id = child.student_account.get_pk()
        orphan = AccountGetter(User.objects.get(username="testorphan"))
        orphan_id = orphan.student_account.get_pk()
        parent = AccountGetter(User.objects.get(username="testparent"))
        self.assertTrue(PermissionChecker.check_permissions(child, child_id))
        self.assertFalse(PermissionChecker.check_permissions(child, orphan_id))
        self.assertTrue(PermissionChecker.check_permissions(parent, child_id))
        self.assertFalse(PermissionChecker.check_permissions(parent, orphan_id))

class AccountGetterTestCase(TestCase):
    def setUp(self):
        suser = User.objects.create_user("teststudent", "", "pwpwpw")
        saccount = Account.objects.create(user=suser, account_type="S", full_name="Test Student")
        sstudent = StudentAccount.objects.create(account=saccount, funds=100)
        puser = User.objects.create_user("testparent", "", "pwpwpw")
        paccount = Account.objects.create(user=puser, account_type="P", full_name="Test Parent")
        pparent = ParentAccount.objects.create(account=paccount)

    def test_parent(self):
        account_getter = AccountGetter(User.objects.get(username="testparent"))
        self.assertEquals(account_getter.parent_account.get_full_name(), "Test Parent")
        self.assertFalse(account_getter.student_account)

    def test_student(self):
        account_getter = AccountGetter(User.objects.get(username="teststudent"))
        self.assertEqual(account_getter.student_account.get_full_name(), "Test Student")
        self.assertFalse(account_getter.parent_account)
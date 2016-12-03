from financeapp.models import Account, StudentAccount, ParentAccount
from financeapp.studentwrapper import StudentWrapper
from financeapp.parentwrapper import ParentWrapper

class AccountGetter:
    def __init__(self, user):
        self.account = Account.objects.get(user=user)
        if self.account.account_type == "S":
            self.student_account = StudentWrapper(StudentAccount.objects.get(account=self.account))
            self.parent_account = False
        else:
            self.parent_account = ParentWrapper(ParentAccount.objects.get(account=self.account))
            self.student_account = False

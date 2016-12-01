from financeapp.models import Account, StudentAccount
from financeapp.studentwrapper import StudentWrapper
class AccountGetter:
    def __init__(self, user):
        self.account = Account.objects.get(user=user)
        if self.account.account_type == "S":
            self.student_account = StudentWrapper(StudentAccount.objects.get(account=self.account))
        else:
            self.student_account = False

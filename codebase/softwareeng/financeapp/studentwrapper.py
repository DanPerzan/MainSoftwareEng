from financeapp.models import Account, StudentAccount

class StudentWrapper:
    def __init__(self, student_account):
        self.student_account = student_account

    def get_pk(self):
        return self.student_account.pk

    def get_account(self):
        return self.student_account.account

    def get_funds(self):
        return self.student_account.funds

    def deposit(self, amount):
        return self.student_account.deposit(amount)
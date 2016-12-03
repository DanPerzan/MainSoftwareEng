from financeapp.models import Account

class AccountWrapper:
    def __init__(self, account):
        self.account = account

    def get_pk(self):
        return self.account.pk

    def get_full_name(self):
        return self.account.get_full_name()

    def get_account(self):
        return self.account.account

    def get_funds(self):
        return self.account.funds

    def deposit(self, amount):
        return self.account.deposit(amount)

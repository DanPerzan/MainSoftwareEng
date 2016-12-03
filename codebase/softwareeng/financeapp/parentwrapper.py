from financeapp.models import Account, StudentAccount
from financeapp.studentwrapper import StudentWrapper

class ParentWrapper:
    def __init__(self, parent_account):
        self.parent_account = parent_account

    def get_pk(self):
        return self.parent_account.pk

    def get_full_name(self):
        return self.parent_account.get_full_name()

    def get_account(self):
        return self.parent_account.account

    def get_children(self):
        children = []
        raw_students = self.parent_account.student_accounts.all()
        for raw_student in raw_students.iterator():
            children.append(StudentWrapper(raw_student))
        return children

    def get_child(self, pk):
        children = self.get_children()
        for child in children:
            if child.get_pk() == int(pk):
                return child
        return False
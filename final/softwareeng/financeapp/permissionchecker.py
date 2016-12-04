class PermissionChecker():
    def check_permissions(account_getter, student_id):
        if (account_getter.student_account):
            return account_getter.student_account.get_pk() == int(student_id)
        else:
            children = account_getter.parent_account.get_children()
            child_found = False
            for child in children:
                if child.get_pk() == int(student_id):
                    child_found = True
            return child_found
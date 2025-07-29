import FileDao

class AccountService:
    def __init__(self):
        self.repo = FileDao.FileService()
    def create_account(self,account_id, name, balance):
        self.repo.openAccount(account_id,name,balance)
    def read_accounts(self):
        self.repo.viewAccounts()
    def update_account(self,account_id, new_name=None, new_balance=None):
        self.repo.updateAccount(account_id,new_name,new_balance)
    def delete_account(self,account_id):
        self.repo.suspendAccount(account_id)
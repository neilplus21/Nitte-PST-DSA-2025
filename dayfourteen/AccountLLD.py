from AccountService import *

if __name__ == "__main__":
    service = AccountService()
    # service.create_account("A001", "John", 1000)
    # service.create_account("A002", "Alice", 1500)
    # service.read_accounts()
    # service.update_account("A001", new_balance=2000)
    # service.delete_account("A002")
    service.read_accounts()

class Bank:
    MAX_ACCOUNTS = 100  # Maximum number of accounts

    def __init__(self):
        self.accounts = []

    def add_account_to_bank(self, account):
        if len(self.accounts) < self.MAX_ACCOUNTS:
            self.accounts.append(account)
            return True
        else:
            print("No more accounts available.")
            return False

    def remove_account_from_bank(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} closed.")
                return True
        print(f"Account not found for account number: {account_number}")
        return False

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None  # Account not found

    def add_monthly_interest(self, interest_rate):
        for account in self.accounts:
            interest = (account.balance * (interest_rate / 100)) / 12
            account.deposit(int(interest))
            print(f"Deposited interest: ${interest:.2f} into account number: {account.account_number}")

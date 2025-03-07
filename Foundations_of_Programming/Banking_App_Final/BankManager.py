from Bank import Bank
from Account import Account
from BankUtility import BankUtility
from CoinCollector import CoinCollector

class BankManager:
    def __init__(self):
        self.bank = Bank()

    def main(self):
        while True:
            print("""
            ============================================================
            What do you want to do?
            1. Open an account
            2. Get account information and balance
            3. Change PIN
            4. Deposit money in account
            5. Transfer money between accounts
            6. Withdraw money from account
            7. ATM withdrawal
            8. Deposit change
            9. Close an account
            10. Add monthly interest to all accounts
            11. End Program
            ============================================================
            """)
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.open_account()
            elif choice == "2":
                self.get_account_info()
            elif choice == "3":
                self.change_pin()
            elif choice == "4":
                self.deposit_money()
            elif choice == "5":
                self.transfer_money()
            elif choice == "6":
                self.withdraw_money()
            elif choice == "7":
                self.atm_withdrawal()
            elif choice == "8":
                self.deposit_change()
            elif choice == "9":
                self.close_account()
            elif choice == "10":
                self.add_interest()
            elif choice == "11":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    def open_account(self):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        ssn = input("Enter SSN (9 digits): ")
        if len(ssn) != 9 or not ssn.isdigit():
            print("Invalid SSN. Must be 9 digits.")
            return
        account = Account(first_name, last_name, ssn)
        if self.bank.add_account_to_bank(account):
            print(account)

    def get_account_info(self):
        account = self.prompt_for_account_number_and_pin()
        if account:
            print(account)

    def change_pin(self):
        account = self.prompt_for_account_number_and_pin()
        if account:
            new_pin = input("Enter new PIN (4 digits): ")
            confirm_pin = input("Enter new PIN again to confirm: ")
            if new_pin == confirm_pin and len(new_pin) == 4 and new_pin.isdigit():
                account.pin = new_pin
                print("PIN updated successfully.")
            else:
                print("PIN mismatch or invalid format. Try again.")

    def deposit_money(self):
        account = self.prompt_for_account_number_and_pin()
        if account:
            amount = float(input("Enter amount to deposit (e.g. 10.50): "))
            account.deposit(int(amount * 100))
            print(f"New balance: ${account.balance / 100:.2f}")

    def deposit_change(self):
        account = self.prompt_for_account_number_and_pin()
        if account:
            coins = input("Deposit coins (P, N, D, Q, H, W): ")
            total_cents = CoinCollector.parse_change(coins)
            if total_cents > 0:
                account.deposit(total_cents)
                print(f"${total_cents / 100:.2f} in coins deposited into account.")
                print(f"New balance: ${account.balance / 100:.2f}")

    def transfer_money(self):
        sender = self.prompt_for_account_number_and_pin()
        if not sender:
            return

        receiver_account_number = int(input("Enter the recipient's account number: "))
        receiver = self.bank.find_account(receiver_account_number)

        if not receiver:
            print("Recipient account not found. Transfer canceled.")
            return

        amount = float(input("Enter amount to transfer (e.g., 10.50): "))
        amount_in_cents = int(amount * 100)

        if sender.withdraw(amount_in_cents):
            receiver.deposit(amount_in_cents)
            print(f"Successfully transferred ${amount:.2f} from Account {sender.account_number} to Account {receiver.account_number}.")
        else:
            print("Transfer failed due to insufficient funds.")

    def withdraw_money(self):
        account = self.prompt_for_account_number_and_pin()
        if account:
            amount = float(input("Enter amount to withdraw (e.g. 10.50): "))
            account.withdraw(int(amount * 100))
            print(f"New balance: ${account.balance / 100:.2f}")

    def add_interest(self):
        while True:
            try:
                interest_rate = float(input("Enter annual interest rate percentage (e.g., 2.75 for 2.75%): "))
                if interest_rate < 0:
                    print("Interest rate cannot be negative. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number (e.g., 2.75).")

        self.bank.add_monthly_interest(interest_rate)
        print("Monthly interest has been added to all accounts.")

    def close_account(self):
        account = self.prompt_for_account_number_and_pin()
        if account:
            self.bank.remove_account_from_bank(account.account_number)

    def prompt_for_account_number_and_pin(self):
        account_number = int(input("Enter account number: "))
        account = self.bank.find_account(account_number)
        if not account:
            print(f"Account not found for account number: {account_number}")
            return None
        pin = input("Enter PIN: ")
        if not account.is_valid_pin(pin):
            print("Invalid PIN.")
            return None
        return account

# Start the program
if __name__ == "__main__":
    manager = BankManager()
    manager.main()

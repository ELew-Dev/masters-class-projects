import random

class Account:
    def __init__(self, first_name, last_name, ssn):
        self.account_number = self.generate_account_number()
        self.owner_first_name = first_name
        self.owner_last_name = last_name
        self.ssn = ssn
        self.pin = self.generate_pin()
        self.balance = 0  # Balance is stored in cents (integer)

    def generate_account_number(self):
        return random.randint(10000000, 99999999)  # 8-digit number

    def generate_pin(self):
        return str(random.randint(1000, 9999))  # 4-digit PIN as a string

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("Amount cannot be negative. Try again.")
            return self.balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient funds or invalid amount.")
            return self.balance

    def is_valid_pin(self, pin):
        return self.pin == pin

    def __repr__(self):
        return f"""
        ============================================
        Account Number: {self.account_number}
        Owner First Name: {self.owner_first_name}
        Owner Last Name: {self.owner_last_name}
        Owner SSN: XXX-XX-{self.ssn[-4:]}  # Hides first 5 digits
        PIN: {self.pin}
        Balance: ${self.balance / 100:.2f}
        ============================================
        """

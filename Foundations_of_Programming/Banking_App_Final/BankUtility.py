import random

class BankUtility:
    
    @staticmethod
    def prompt_user_for_string(prompt):
        """Prompts the user for a string input and returns it."""
        return input(prompt)

    @staticmethod
    def prompt_user_for_positive_number(prompt):
        """Prompts the user for a positive number and ensures it is valid."""
        while True:
            try:
                amount = float(input(prompt))
                if amount > 0:
                    return amount
                else:
                    print("Amount cannot be negative or zero. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    @staticmethod
    def generate_random_integer(min_value, max_value):
        """Generates a random integer between min_value and max_value (inclusive)."""
        return random.randint(min_value, max_value)

    @staticmethod
    def convert_from_dollars_to_cents(amount):
        """Converts a dollar amount to cents (e.g., $3.57 → 357 cents)."""
        return int(amount * 100)

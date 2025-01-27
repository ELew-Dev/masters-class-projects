import random

def generate_random_number(min_num, max_num):
    """
    Generates a random number between min_num and max_num (inclusive).
    """
    return random.randint(min_num, max_num)

def check_guess(random_num, user_guess):
    """
    Checks if the user's guess matches the random number.
    Returns True if correct, False otherwise.
    """
    return user_guess == random_num

def provide_hint(random_num):
    """
    Provides a random hint to the user after 2 incorrect guesses.
    """
    hints = [
        f"Hint: The number is {'even' if random_num % 2 == 0 else 'odd'}.",
        f"Hint: The number is{' ' if random_num % 5 == 0 else ' not '}a multiple of 5.",
        f"Hint: The number squared is {'greater' if random_num ** 2 > 1000 else 'less'} than 1,000."
    ]
    return random.choice(hints)

def main():
    print("Welcome to the Guess the Number Game!")
    print("I have selected a random number between 1 and 100. Try to guess it!")

    random_num = generate_random_number(1, 100)
    attempts = 0
    incorrect_guesses = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if check_guess(random_num, guess):
                print(f"Correct! You guessed the number in {attempts} attempts.")
                break
            else:
                incorrect_guesses += 1
                if guess < random_num:
                    print("Incorrect! Try a higher number.")
                else:
                    print("Incorrect! Try a lower number.")

                if incorrect_guesses == 2:
                    print(provide_hint(random_num))
        
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

if __name__ == "__main__":
    main()

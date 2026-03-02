#guessing game
import random

def number_guessing_game():
    print(" \n ---------Welcome to the Number Guessing Game!---------")
    print("I'm thinking of a number between 1 and 100.")

    # Generate random number
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess number: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                if attempts <= 3:
                    print("Brilliant! You guessed within 3 attempts!")
                    break
                else:
                    print(f"Great! You guessed it in {attempts} attempts.")
                    break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

number_guessing_game()
import sys
import random
import time

while True:

    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Can you guess it?")
    print("You have 5 attempts to guess the number. Good luck!")

    print("please select a difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (5 attempts)")
    print("3. Hard (3 attempts)")

    print("Enter your choice (1, 2, or 3):")

    try:
        choice = int(input())
    except ValueError:
        print("Please enter a valid number.")
        continue

    mx = 0

    if choice == 1:
        print("You have selected Easy difficulty. You have 10 attempts to guess the number.")
        mx = 10
    elif choice == 2:
        print("You have selected Medium difficulty. You have 5 attempts to guess the number.")
        mx = 5
    elif choice == 3:
        print("You have selected Hard difficulty. You have 3 attempts to guess the number.")
        mx = 3
    else:
        print("Invalid choice. Please select a valid difficulty level.")
        continue

    print("Lets start the game")

    num = random.randint(1, 100)
    attempts = 0
    wrong_guesses = 0

    start_time = time.time()

    while attempts < mx:

        print("Enter your guess:")

        try:
            guess = int(input())
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < num:
            print("Too low! Try again.")
            wrong_guesses += 1

        elif guess > num:
            print("Too high! Try again.")
            wrong_guesses += 1

        else:
            print(f"Congratulations! You've guessed the number {num} in {attempts} attempts!")
            break

        print(f"Attempts left: {mx - attempts}")

        if wrong_guesses == 3:
            if num % 2 == 0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")

        if wrong_guesses == 5:
            if num > 50:
                print("Hint: The number is greater than 50.")
            else:
                print("Hint: The number is 50 or less.")

    if attempts == mx and guess != num:
        print(f"Game over! You've used all {mx} attempts. The number was {num}. Better luck next time!")

    end_time = time.time()
    print(f"Game completed in {end_time - start_time:.2f} seconds.")

    play_again = input("Do you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("Thanks for playing!")
        break
import random

print("====================================")
print("       NUMBER GUESSING GAME")
print("====================================")

print("I have chosen a number between 1 and 100.")
print("Try to guess the number!")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Keep track of the number of attempts
attempts = 0

while True:
    try:
        # Ask the user for a guess
        guess = int(input("Enter your guess: "))

        # Increase attempt count
        attempts += 1

        # Check whether the guess is valid
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        # Check the guess
        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print()
            print("Congratulations! You guessed the correct number.")
            print(f"The number was {secret_number}.")
            print(f"You found it in {attempts} attempts.")
            break

    except ValueError:
        print("Invalid input. Please enter a whole number.")

print()
print("Thank you for playing!")
print("====================================")
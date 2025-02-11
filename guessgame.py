import random

random_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Guessing Game!")
print("Guess a number between 1 and 100.")

while True:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess > random_number:
            print("higher value! Try again.")
        elif user_guess < random_number:
            print("lower value! Try again.")
        else:
            print("Congratulations! You guessed the number in attempts: %d ",attempts)
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

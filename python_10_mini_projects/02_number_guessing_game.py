import random

secret = random.randint(1, 100)
attempts = 0

print("Guess a number between 1 and 100!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You won in {attempts} attempts.")
        break

import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess 1-100: "))
    attempts += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! Attempts: {attempts}")
        break

# We are going to write a program that generates a random number and asks the user to 
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower number please”. 
# Similarly, if the user’s guess is too low, the program prints “higher 
# number please” When the user guesses the correct number, the program displays the 
# number of guesses the player used to arrive at the number.

import random 
n = random.randint(1 , 100)
guess = 0

a = -1
while(a!=n):
    guess += 1
    a = int(input("enter your number : "))
    if (a>n):
        print("lower number pls")
    else:
        print("hihger number pls")
print (f"you have guessed the right number {n} in {guess} guesses ")



import random
choices = ["rock", "paper", "scissors"]
u = c = 0
for i in range(5):
    user = input("rock/paper/scissors: ").lower()
    if user not in choices: continue
    comp = random.choice(choices)
    print("Computer:", comp)
    if user == comp: print("Draw!")
    elif (user, comp) in [("rock","scissors"),("paper","rock"),("scissors","paper")]:
        u += 1; print("You win!")
    else:
        c += 1; print("Computer wins!")
print("Score:", u, "-", c)

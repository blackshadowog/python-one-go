balance = 1000.0

while True:
    print("\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        print(f"Balance: ₹{balance:.2f}")
    elif choice == "2":
        amount = float(input("Deposit amount: "))
        if amount > 0:
            balance += amount
            print("Deposit successful.")
    elif choice == "3":
        amount = float(input("Withdraw amount: "))
        if 0 < amount <= balance:
            balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance or invalid amount.")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")

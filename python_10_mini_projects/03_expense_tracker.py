expenses = []

while True:
    print("\n1. Add expense\n2. Show expenses\n3. Total\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        expenses.append((name, amount))
        print("Expense added.")
    elif choice == "2":
        for name, amount in expenses:
            print(f"{name}: ₹{amount:.2f}")
    elif choice == "3":
        print(f"Total: ₹{sum(a for _, a in expenses):.2f}")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")

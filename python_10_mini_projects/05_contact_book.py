contacts = {}

while True:
    print("\n1. Add contact\n2. Search contact\n3. Show all\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        contacts[name] = phone
        print("Saved.")
    elif choice == "2":
        name = input("Name to search: ").strip()
        print(contacts.get(name, "Contact not found."))
    elif choice == "3":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")

tasks = []

while True:
    print("\n1. Add task\n2. View tasks\n3. Complete task\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        tasks.append({"task": input("Task: "), "done": False})
    elif choice == "2":
        if not tasks:
            print("No tasks.")
        for i, item in enumerate(tasks, 1):
            status = "✓" if item["done"] else " "
            print(f"{i}. [{status}] {item['task']}")
    elif choice == "3":
        number = int(input("Task number: ")) - 1
        if 0 <= number < len(tasks):
            tasks[number]["done"] = True
            print("Task completed.")
        else:
            print("Invalid task.")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")

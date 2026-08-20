while True:
    s = input("Enter: number operator number (q to quit): ")
    if s.lower() == "q": break
    try:
        a, op, b = s.split()
        a, b = float(a), float(b)
        if op == "+": r = a+b
        elif op == "-": r = a-b
        elif op == "*": r = a*b
        elif op == "/": r = "Cannot divide by zero" if b == 0 else a/b
        else: r = "Invalid operator"
        print("Result:", r)
    except ValueError:
        print("Example: 10 + 5")

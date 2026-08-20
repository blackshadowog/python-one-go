stock = {}
while True:
    print("1 Add  2 Sell  3 View  4 Exit")
    ch = input("Choose: ")
    if ch == "1":
        item = input("Item: ")
        stock[item] = stock.get(item, 0) + int(input("Quantity: "))
    elif ch == "2":
        item = input("Item: ")
        qty = int(input("Quantity: "))
        if stock.get(item, 0) >= qty: stock[item] -= qty
        else: print("Not enough stock.")
    elif ch == "3":
        for item, qty in stock.items(): print(item, qty)
    elif ch == "4": break

import random, string
urls = {}
while True:
    print("1 Shorten  2 Open  3 View  4 Exit")
    ch = input("Choose: ")
    if ch == "1":
        url = input("URL: ")
        code = "".join(random.choices(string.ascii_letters+string.digits, k=6))
        urls[code] = url
        print("short.local/" + code)
    elif ch == "2":
        print(urls.get(input("Code: "), "Not found"))
    elif ch == "3":
        for c,u in urls.items(): print(f"short.local/{c} -> {u}")
    elif ch == "4": break

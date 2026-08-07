try:
    a= int(input("enter your number: "))
    b = int(input("enter your number: "))
    c = a/b
    print(c)

except ZeroDivisionError as v:
    print("b can not be zero")


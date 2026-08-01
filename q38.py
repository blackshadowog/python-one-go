
def function():
    if(a>b and a>c):
        return a
    elif(b>b and a>c):
        return b
    elif(c>a and c>b):
        return c
    
a = int(input("number : "))
b = int(input("number : "))
c = int(input("number : "))

print("greatest of a b c :", function())

n = int(input("enter your number: "))

table = [n*i  for i in range(1,11)]
print(table)
with open("tables.txt" , "a") as f:
    f.write(str(table) + "\n") 
    print("")
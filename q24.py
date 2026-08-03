p1 = "e sala cup namde"
p2 = "rcb  won the ipl"
p3 = "rcb makes the history"

news = input(" enter your news : ")

if((p1 in news) or (p2 in news) or (p3 in news)):
    print("this news contains spam")

else:
    print("news is trust full")
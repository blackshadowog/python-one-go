def remo(l,word):
        n=[]
        for item in l:
         if not (item == word):
            n.append(item.strip(word))
         return n

l = ["ani","vani","ram", "ni"]
print(remo(l, "ni"))
def remo(l,word):
        for item in l:
         l.remove(word)
         return l

l = ["ani","vani","ram", "bb"]
print(remo(l, "bb"))
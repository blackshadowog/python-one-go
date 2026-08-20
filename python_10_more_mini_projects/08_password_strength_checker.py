import string
p = input("Password: ")
score = sum([len(p)>=8, any(c.isupper() for c in p), any(c.islower() for c in p), any(c.isdigit() for c in p), any(c in string.punctuation for c in p)])
levels = ["Very Weak","Weak","Fair","Good","Strong","Very Strong"]
print("Strength:", levels[score])

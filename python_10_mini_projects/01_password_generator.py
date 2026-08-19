import secrets
import string

length = int(input("Password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(secrets.choice(chars) for _ in range(length))
print("Generated password:", password)

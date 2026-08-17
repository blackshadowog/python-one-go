import secrets
import string

length = 16
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(chars) for _ in range(length))
print("Secure password:", password)

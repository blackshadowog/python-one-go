text = input("Enter text: ")
clean = ''.join(c.lower() for c in text if c.isalnum())

print("Palindrome" if clean == clean[::-1] else "Not a palindrome")

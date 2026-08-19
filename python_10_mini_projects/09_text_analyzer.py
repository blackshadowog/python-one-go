text = input("Enter text: ")

words = text.split()
characters = len(text)
letters = sum(c.isalpha() for c in text)
digits = sum(c.isdigit() for c in text)

print("\n--- Text Analysis ---")
print("Words:", len(words))
print("Characters:", characters)
print("Letters:", letters)
print("Digits:", digits)

if words:
    print("Average word length:", round(sum(map(len, words)) / len(words), 2))

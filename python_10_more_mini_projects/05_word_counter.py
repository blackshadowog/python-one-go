from collections import Counter
text = input("Enter text: ")
words = [w.strip(".,!?;:").lower() for w in text.split()]
print("Total words:", len(words))
print("Unique words:", len(set(words)))
print("Top words:", Counter(words).most_common(5))

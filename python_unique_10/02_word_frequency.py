from collections import Counter
import re

text = input("Enter a sentence: ").lower()
words = re.findall(r"\b\w+\b", text)
for word, count in Counter(words).most_common():
    print(f"{word}: {count}")

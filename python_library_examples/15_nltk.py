import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")
text = "Python is amazing!"
print(word_tokenize(text))

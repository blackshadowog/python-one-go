import spacy

nlp = spacy.blank("en")
doc = nlp("Python is powerful.")
for token in doc:
    print(token.text)

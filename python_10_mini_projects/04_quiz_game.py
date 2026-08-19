questions = [
    ("Which language is used for AI and data science?", "python"),
    ("What does CPU stand for?", "central processing unit"),
    ("Which keyword creates a function in Python?", "def"),
    ("What is 10 + 5?", "15")
]

score = 0

for question, answer in questions:
    user = input(question + " ").strip().lower()
    if user == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"\nFinal Score: {score}/{len(questions)}")

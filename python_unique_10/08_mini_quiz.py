questions = {
    "Capital of France? ": "paris",
    "5 * 8 = ": "40",
    "Python file extension? ": ".py",
}

score = 0
for question, answer in questions.items():
    if input(question).strip().lower() == answer:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")

print(f"Score: {score}/{len(questions)}")

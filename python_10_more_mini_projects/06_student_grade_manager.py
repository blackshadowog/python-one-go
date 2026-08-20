students = {}
while True:
    print("1 Add  2 Show  3 Exit")
    ch = input("Choose: ")
    if ch == "1":
        name = input("Name: ")
        marks = [float(input(f"Subject {i+1}: ")) for i in range(3)]
        avg = sum(marks)/3
        grade = "A+" if avg >= 90 else "A" if avg >= 80 else "B" if avg >= 70 else "C" if avg >= 60 else "D"
        students[name] = avg, grade
    elif ch == "2":
        for n, (a,g) in students.items(): print(f"{n}: {a:.1f}% - {g}")
    elif ch == "3": break

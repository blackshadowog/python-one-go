import matplotlib.pyplot as plt
from sympy import true

# Data
subjects = ["Math", "Science", "English", "Computer"]
marks = [85, 90, 78, 95]

# Create bar chart
plt.bar(subjects, marks, color="skyblue")

# Title and labels
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")


# Display chart
plt.show()
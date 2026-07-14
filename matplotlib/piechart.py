import matplotlib.pyplot as plt

# Data
subjects = ["Math", "Science", "English", "Computer"]
marks = [85, 90, 78, 95]

# Create pie chart
plt.pie(marks, labels=subjects, autopct="%1.1f%%")

# Title
plt.title("Student Marks Distribution")

# Display chart
plt.show()
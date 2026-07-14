import matplotlib.pyplot as plt

# Data
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# Create box plot
plt.boxplot(marks)

# Title and labels
plt.title("Box Plot of Student Marks")
plt.ylabel("Marks")

# Display chart
plt.show()
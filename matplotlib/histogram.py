import matplotlib.pyplot as plt

# Data
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 75, 80, 65, 70]

# Create histogram
plt.hist(marks, bins=5, color="skyblue", edgecolor="black")

# Title and labels
plt.title("Histogram of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

# Display chart
plt.show()
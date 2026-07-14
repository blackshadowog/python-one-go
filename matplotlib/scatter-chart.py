import matplotlib.pyplot as plt

# X and Y values
x = [10, 20, 30, 40, 50, 60]
y = [15, 25, 35, 30, 45, 55]

# Create scatter plot
plt.scatter(x, y, color="blue", marker="o", s=100 , alpha=0.7, edgecolors="black")

# Chart title and labels
plt.title("Student Marks Scatter Plot")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")

# Show grid
plt.grid(True)

# Display chart
plt.show()
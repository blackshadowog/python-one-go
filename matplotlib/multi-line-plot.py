import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# First line
plt.plot(x, y1, label="Line 1", color="blue")

# Second line
plt.plot(x, y2, label="Line 2", color="red")

# Title and labels
plt.title("Two Lines in One Figure")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show legend
plt.legend()

# Grid
plt.grid(True)

# Display graph
plt.show()
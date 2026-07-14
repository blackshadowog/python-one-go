import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

# Create subplots (1 row, 2 columns)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# First plot
ax[0].plot(x, y1)
ax[0].set_title("Line Chart")
ax[0].set_xlabel("X")
ax[0].set_ylabel("Y")

# Second plot
ax[1].plot(x, y2)
ax[1].set_title("Square Values")
ax[1].set_xlabel("X")
ax[1].set_ylabel("Y")

plt.tight_layout()
plt.show()
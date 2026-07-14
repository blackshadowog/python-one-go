import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

fig, ax = plt.subplots(2, 2, figsize=(8, 6))

# Line Plot
ax[0, 0].plot(x, y)
ax[0, 0].set_title("Line Plot")

# Bar Chart
ax[0, 1].bar(x, y)
ax[0, 1].set_title("Bar Chart")

# Scatter Plot
ax[1, 0].scatter(x, y)
ax[1, 0].set_title("Scatter Plot")

# Histogram
ax[1, 1].hist(y, bins=5)
ax[1, 1].set_title("Histogram")

plt.tight_layout()
plt.show()
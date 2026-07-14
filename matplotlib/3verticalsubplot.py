import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

fig, ax = plt.subplots(3, 1, figsize=(6, 8))

ax[0].plot(x, y)
ax[0].set_title("Line Chart")

ax[1].bar(x, y)
ax[1].set_title("Bar Chart")

ax[2].scatter(x, y)
ax[2].set_title("Scatter Plot")

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y, color="red", linewidth=2, linestyle="--", marker="o")
plt.title("Line Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
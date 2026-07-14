import matplotlib.pyplot as plt

# Sample Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Common Styles
styles = [
    "classic",
    "ggplot",
    "bmh",
    "dark_background",
    "fivethirtyeight",
    "grayscale",
    "fast",
    "Solarize_Light2",
    "seaborn-v0_8",
    "tableau-colorblind10"
]

# Display each style
for style in styles:
    plt.style.use(style)

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, marker="o", label="Data")
    plt.title(f"Style: {style}")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)

    plt.show()
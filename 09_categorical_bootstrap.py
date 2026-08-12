import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.pointplot(
    data=df,
    x="day",
    y="total_bill",
    hue="sex",
    errorbar=("ci", 95),
    estimator="mean",
    capsize=.15,
    dodge=.25
)

plt.title("Mean Bill with 95% Confidence Intervals")
plt.xlabel("Day")
plt.ylabel("Mean Total Bill")
plt.tight_layout()
plt.show()

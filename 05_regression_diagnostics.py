import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

g = sns.lmplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="smoker",
    col="time",
    row="sex",
    height=4,
    scatter_kws={"alpha": 0.5},
    line_kws={"linewidth": 2}
)

g.set_axis_labels("Total Bill", "Tip")
g.fig.suptitle("Regression Diagnostics by Segment", y=1.02)
plt.show()

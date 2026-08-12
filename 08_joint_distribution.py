import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("diamonds").sample(3000, random_state=42)

g = sns.jointplot(
    data=df,
    x="carat",
    y="price",
    kind="hex",
    height=8,
    color="steelblue"
)

g.plot_joint(sns.kdeplot, levels=6, linewidths=1)
g.set_axis_labels("Carat", "Price")
plt.show()

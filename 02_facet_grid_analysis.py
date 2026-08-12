import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

g = sns.FacetGrid(df, col="time", row="sex", hue="smoker", margin_titles=True)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip", alpha=0.7)
g.add_legend()
g.set_axis_labels("Total Bill", "Tip")
plt.show()

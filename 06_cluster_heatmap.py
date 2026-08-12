import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
numeric = df.drop(columns="species")

g = sns.clustermap(
    numeric.corr(),
    annot=True,
    cmap="coolwarm",
    center=0,
    linewidths=.5,
    figsize=(8, 7)
)
g.fig.suptitle("Hierarchical Clustering of Feature Correlations", y=1.02)
plt.show()

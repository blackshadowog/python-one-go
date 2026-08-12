import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins").select_dtypes("number")
corr = df.corr(method="spearman")

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="vlag",
    center=0,
    linewidths=.5,
    square=True
)
plt.title("Spearman Correlation Heatmap")
plt.tight_layout()
plt.show()

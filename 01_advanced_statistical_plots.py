import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins").dropna()
sns.set_theme(style="whitegrid")

sns.pairplot(df, hue="species", diag_kind="kde", corner=True)
plt.suptitle("Advanced Pairwise Analysis", y=1.02)
plt.show()

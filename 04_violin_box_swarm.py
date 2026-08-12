import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

fig, ax = plt.subplots(figsize=(10, 6))
sns.violinplot(data=df, x="day", y="total_bill", inner=None, ax=ax)
sns.boxplot(data=df, x="day", y="total_bill", width=.18, ax=ax)
sns.stripplot(data=df, x="day", y="total_bill", size=3, alpha=.35, ax=ax)

ax.set_title("Distribution + Quartiles + Individual Observations")
plt.tight_layout()
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks")
df = sns.load_dataset("penguins").dropna()

fig = plt.figure(figsize=(14, 9))
gs = fig.add_gridspec(2, 2)

ax1 = fig.add_subplot(gs[0, 0])
sns.scatterplot(
    data=df, x="bill_length_mm", y="bill_depth_mm",
    hue="species", size="body_mass_g", ax=ax1
)
ax1.set_title("Bill Dimensions")

ax2 = fig.add_subplot(gs[0, 1])
sns.boxplot(data=df, x="species", y="body_mass_g", ax=ax2)
ax2.set_title("Body Mass Distribution")

ax3 = fig.add_subplot(gs[1, 0])
corr = df.select_dtypes("number").corr()
sns.heatmap(corr, annot=True, fmt=".2f", center=0, ax=ax3)
ax3.set_title("Feature Correlations")

ax4 = fig.add_subplot(gs[1, 1])
sns.kdeplot(
    data=df, x="body_mass_g", hue="species",
    fill=True, common_norm=False, alpha=.25, ax=ax4
)
ax4.set_title("Body Mass Density")

fig.suptitle("Seaborn Advanced Analytics Dashboard", fontsize=16)
plt.tight_layout()
plt.show()

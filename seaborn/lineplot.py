import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("tips")
df.head()
sns.lineplot(x="total_bill", y="tip", data=df , hue="sex")
plt.show()
#heatmap
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("tips")
corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True)
plt.show()

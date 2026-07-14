import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=df)
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("flights")
df["date"] = pd.to_datetime(
    df["year"].astype(str) + "-" + df["month"].astype(str)
)

sns.lineplot(data=df, x="date", y="passengers", marker="o")
plt.fill_between(
    df["date"],
    df["passengers"],
    alpha=0.12
)
plt.title("Monthly Airline Passenger Trend")
plt.xlabel("Date")
plt.ylabel("Passengers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

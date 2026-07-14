import pandas as pd
 # 2 methods to read data from a file
 # head() and tail()
df = pd.read_csv("data.csv" , encoding="latin-1")
print(df.head(10)) # first 10 rows
print(df.tail(10)) # last 10 rows
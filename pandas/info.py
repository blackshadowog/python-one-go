# info of data
import pandas as pd 
df = pd.read_csv("data.csv" , encoding="latin-1")
print(df.info())
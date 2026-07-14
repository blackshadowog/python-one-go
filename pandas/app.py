import pandas as pd
# # CSV Read
df = pd.read_csv("data.csv", encoding="latin-1")
print(df)

# # Excel Read
dfexcel = pd.read_excel("data.xls", engine="openpyxl")
print(dfexcel)

# # JSON Read
dfjson = pd.read_json("data.json")
print(dfjson)



import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],    
    "Age": [25, 30, 35],    
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)
# Save to CSV
df.to_csv("output.csv", index=False)
df.to_excel ("output.xlsx", index=False)
df.to_json("output.json" , index=False)
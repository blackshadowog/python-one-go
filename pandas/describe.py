import pandas as pd    
data = {
    "Name": ["Alice", "Bob", "Charlie" , "David", "Eve"],    
    "Age": [25, 30, 35 , 40, 45],
    "salary": [50000, 60000, 70000 , 80000, 90000],
    "performance": ["A", "B", "C" , "D", "E"],
    "City": ["New York", "Los Angeles", "Chicago" , "Houston", "Phoenix"]
}
df = pd.DataFrame(data)
print(df)
# descriptive statistics
print(df.describe())
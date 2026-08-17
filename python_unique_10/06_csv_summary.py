import csv
from pathlib import Path

file = Path(input("CSV file: "))

with file.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print("Rows:", len(rows))
print("Columns:", list(rows[0].keys()) if rows else [])
for row in rows[:5]:
    print(row)

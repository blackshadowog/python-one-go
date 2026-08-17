from pathlib import Path
from collections import defaultdict
import hashlib

folder = Path(input("Folder path: "))
groups = defaultdict(list)

for file in folder.rglob("*"):
    if file.is_file():
        digest = hashlib.sha256(file.read_bytes()).hexdigest()
        groups[digest].append(file)

for files in groups.values():
    if len(files) > 1:
        print("\nDuplicate group:")
        for file in files:
            print(" ", file)

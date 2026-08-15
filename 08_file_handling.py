from pathlib import Path

path = Path("demo.txt")
path.write_text("Python file handling!")
print(path.read_text())
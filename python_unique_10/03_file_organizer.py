from pathlib import Path
import shutil

folder = Path(input("Folder path: "))
for file in folder.iterdir():
    if file.is_file():
        category = file.suffix[1:].upper() or "NO_EXTENSION"
        target = folder / category
        target.mkdir(exist_ok=True)
        shutil.move(str(file), target / file.name)

print("Files organized.")

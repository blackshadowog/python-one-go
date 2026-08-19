from pathlib import Path
import shutil

folder = Path(input("Folder path: ")).expanduser()

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"]
}

for file in folder.iterdir():
    if not file.is_file():
        continue

    category = next(
        (name for name, extensions in categories.items()
         if file.suffix.lower() in extensions),
        "Others"
    )

    target = folder / category
    target.mkdir(exist_ok=True)
    shutil.move(str(file), str(target / file.name))

print("Files organized successfully!")

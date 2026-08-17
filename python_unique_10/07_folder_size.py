from pathlib import Path

folder = Path(input("Folder path: "))
total = sum(p.stat().st_size for p in folder.rglob("*") if p.is_file())

units = ["B", "KB", "MB", "GB", "TB"]
size = float(total)
for unit in units:
    if size < 1024 or unit == units[-1]:
        print(f"Total size: {size:.2f} {unit}")
        break
    size /= 1024

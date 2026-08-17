import json
from pathlib import Path

file = Path("notes.json")
notes = json.loads(file.read_text(encoding="utf-8")) if file.exists() else []

note = input("New note: ").strip()
if note:
    notes.append({"text": note})
    file.write_text(json.dumps(notes, indent=2), encoding="utf-8")

print("\n".join(f"{i+1}. {n['text']}" for i, n in enumerate(notes)))

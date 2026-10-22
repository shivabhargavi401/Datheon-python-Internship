import os
import shutil
from pathlib import Path

CATEGORIES = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".py": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code"
}

def organize(folder):
    folder = Path(folder).resolve()
    moved = 0
    skipped = 0

    if not folder.is_dir():
        print("Error: Folder does not exist.")
        return

    for entry in os.scandir(folder):
        if not entry.is_file():
            continue

        source = Path(entry.path)

        # Avoid moving the organizer script itself
        if source.resolve() == Path(__file__).resolve():
            continue

        category = CATEGORIES.get(source.suffix.lower())

        if not category:
            skipped += 1
            continue

        destination_folder = folder / category
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / source.name

        # Avoid overwriting files with the same name
        if destination.exists():
            print(f"Skipped duplicate: {source.name}")
            skipped += 1
            continue

        try:
            shutil.move(str(source), str(destination))
            print(f"Moved: {source.name} -> {category}/")
            moved += 1
        except (PermissionError, OSError) as error:
            print(f"Could not move {source.name}: {error}")
            skipped += 1

    print("\n--- ORGANIZATION SUMMARY ---")
    print(f"Files moved: {moved}")
    print(f"Files skipped: {skipped}")

if __name__ == "__main__":
    target = input("Enter the folder path to organize: ").strip().strip('"')
    organize(target)
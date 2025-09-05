import os
import shutil

# Root folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Destination assets folder
DEST_DIR = os.path.join(ROOT_DIR, "assets")

# Categories and keywords
CATEGORIES = {
    "entities": ["class Player", "class Zombie", "class Creeper", "Block", "Entity"],
    "logic": ["def tick", "worldgen", "AI", "physics", "update("],
    "rendering": ["render", "draw", "texture", "ursina"],
    "input": ["key", "mouse", "input"],
    "networking": ["socket", "packet", "server", "client"],
    "audio": ["sound", "music", "pygame.mixer"],
    "utils": ["math", "util", "helper"],
}

# Files/folders to skip
SKIP = ["organizer.py", "README.txt", "assets"]

def detect_category(filepath):
    try:
        with open(filepath, "r", errors="ignore") as f:
            code = f.read()
            for category, keywords in CATEGORIES.items():
                if any(keyword in code for keyword in keywords):
                    return category
    except:
        pass
    return "misc"

def organize_files():
    os.makedirs(DEST_DIR, exist_ok=True)
    
    # Walk the root folder recursively
    for root, dirs, files in os.walk(ROOT_DIR):
        # Skip the assets folder itself
        if "assets" in root:
            continue
        for file in files:
            if file.endswith(".py") and file not in SKIP:
                src_path = os.path.join(root, file)
                category = detect_category(src_path)
                dest_folder = os.path.join(DEST_DIR, category)
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, file)
                shutil.move(src_path, dest_path)
                print(f"Moved {file} -> {category}")
    
    # Remove empty batch folders
    for dir_name in os.listdir(ROOT_DIR):
        dir_path = os.path.join(ROOT_DIR, dir_name)
        if os.path.isdir(dir_path) and dir_name.startswith("batch_"):
            try:
                shutil.rmtree(dir_path)
                print(f"Deleted empty folder {dir_name}")
            except:
                pass

if __name__ == "__main__":
    organize_files()
    print("✅ Done! All scripts from batches moved into assets/ and root is clean.")
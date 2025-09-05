import os
import re
import shutil
import csv

# Root folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")

# Output mapping file
MAPPING_FILE = os.path.join(ROOT_DIR, "mapping.csv")

# Simple rules for suggested names (you can expand)
KEYWORDS = {
    "Player": ["Player", "player", "entity", "mob"],
    "Block": ["Block", "block", "tile"],
    "World": ["World", "world", "chunk"],
    "Zombie": ["Zombie", "mob", "hostile"],
    "Renderer": ["render", "draw", "texture"],
    "Network": ["socket", "packet", "server", "client"],
    "Audio": ["sound", "music", "pygame.mixer"],
    "Utils": ["math", "helper", "util"]
}

# Detect class names and suggest new file names
def suggest_name(filepath):
    try:
        with open(filepath, "r", errors="ignore") as f:
            content = f.read()
            # Search for class definitions
            class_match = re.findall(r"class (\w+)", content)
            if class_match:
                name = class_match[0]
                return name
            # Search for keywords if no class
            for sug_name, kws in KEYWORDS.items():
                for kw in kws:
                    if kw in content:
                        return sug_name
    except:
        pass
    return os.path.splitext(os.path.basename(filepath))[0]  # default to original

# Update imports in all files
def update_imports(mapping):
    for root, _, files in os.walk(ASSETS_DIR):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "r", errors="ignore") as f:
                    content = f.read()
                for old, new in mapping.items():
                    if old != new:
                        # Update simple import statements
                        content = re.sub(rf"from {re.escape(old)} import", f"from {new} import", content)
                        content = re.sub(rf"import {re.escape(old)}", f"import {new}", content)
                with open(path, "w", errors="ignore") as f:
                    f.write(content)

# Main function
def organize_and_rename():
    mapping = {}
    for root, _, files in os.walk(ASSETS_DIR):
        for file in files:
            if file.endswith(".py"):
                old_path = os.path.join(root, file)
                suggested_name = suggest_name(old_path)
                new_file = suggested_name + ".py"
                new_path = os.path.join(root, new_file)
                if old_path != new_path:
                    shutil.move(old_path, new_path)
                    print(f"Renamed {file} -> {new_file}")
                mapping[os.path.splitext(file)[0]] = os.path.splitext(new_file)[0]
    
    # Update imports across all scripts
    update_imports(mapping)
    
    # Save mapping to CSV
    with open(MAPPING_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["old_name", "new_name"])
        for old, new in mapping.items():
            writer.writerow([old, new])
    print(f"✅ Done! Mapping saved to {MAPPING_FILE}")

if __name__ == "__main__":
    organize_and_rename()
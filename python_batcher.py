import os
import shutil

# Path to your MOSP PythonWrappers folder
MOSP_FOLDER = os.path.expanduser("~/Downloads/MOSP/PythonWrappers")

# Output folder for batches (inside PythonWrappers)
OUTPUT_FOLDER = os.path.join(MOSP_FOLDER, "batches")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# List all Python files
files = [f for f in os.listdir(MOSP_FOLDER) if f.endswith(".py")]

batch_size = 100
batch_num = 1

for i in range(0, len(files), batch_size):
    batch_path = os.path.join(OUTPUT_FOLDER, f"batch_{batch_num}")
    os.makedirs(batch_path, exist_ok=True)
    for f in files[i:i+batch_size]:
        shutil.copy(os.path.join(MOSP_FOLDER, f), batch_path)
    batch_num += 1

print(f" Created {batch_num-1} batches in {OUTPUT_FOLDER}")
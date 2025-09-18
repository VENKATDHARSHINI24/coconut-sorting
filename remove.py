import os
import glob

# Folder path
folder = "C:\Users\venka\Downloads\coconut (4)\coconut\coconut\new_dataset\healthy"

# Remove all .txt files
for file in glob.glob(os.path.join(folder, "*.txt")):
    os.remove(file)
    print(f"Removed: {file}")

import os
from collections import Counter

DATASET_PATH = "../../dataset/raw/images"

files = os.listdir(DATASET_PATH)

classes = []

for file in files:
    if file.endswith(".jpg"):
        breed = "_".join(file.split("_")[:-1])
        classes.append(breed)

counter = Counter(classes)

print(f"Total Images: {len(files)}")
print(f"Total Classes: {len(counter)}")

print("\nClass Distribution:\n")

for cls, count in sorted(counter.items()):
    print(f"{cls}: {count}")
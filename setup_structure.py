import os

# Root folder (your current project)
root = "."

# ---- Basic, clean structure ----
folders = [
    "data",
    "notebooks",
    "src",
    "experiments",
    "outputs",
    "scripts"
]

files = {
    "requirements.txt": "",
    "src/__init__.py": "",
    "src/dataset_loader.py": "# dataset loading logic will go here\n",
    "src/preprocess.py": "# preprocessing utilities\n",
    "src/train.py": "# training logic\n",
    "src/evaluate.py": "# evaluation metrics\n",
    "src/utils.py": "# helper functions\n",
    "scripts/run_experiment.py": "# example script to launch experiments\n",
}

# Create folders
for folder in folders:
    os.makedirs(os.path.join(root, folder), exist_ok=True)

# Create files
for path, content in files.items():
    file_path = os.path.join(root, path)
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("✅ Base project structure created successfully inside 'Exploring-Model-Performance/'!")

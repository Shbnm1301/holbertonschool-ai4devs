import os

folder = "bug_snippets"

if os.path.exists(folder):
    files = os.listdir(folder)
else:
    files = []

files = [f for f in files if os.path.isfile(os.path.join(folder, f))]

print("Number of files:", len(files))

for file in files:
    path = os.path.join(folder, file)

    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            print(f"{file} -> {len(f.readlines())} lines")
    except:
        pass
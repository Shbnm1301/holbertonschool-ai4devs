import os

base_dir = os.getcwd()
folder = os.path.join(base_dir, "bug_snippets")

files = os.listdir(folder)
files = [f for f in files if f.endswith((".py", ".js", ".java"))]

print("Number of files:", len(files))

for file in files:
    path = os.path.join(folder, file)

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        print(file, "->", len(f.readlines()), "lines")

import os
import sys

print("SCRIPT STARTED")

base_dir = os.path.dirname(__file__)
folder = os.path.join(base_dir, "bug_snippets")

if not os.path.exists(folder):
    print("ERROR: bug_snippets NOT FOUND at", folder)
    sys.exit(1)

files = os.listdir(folder)
files = [f for f in files if f.endswith((".py", ".js", ".java"))]

print("Number of files:", len(files))
print()

for file in files:
    path = os.path.join(folder, file)

    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            print(file, "->", len(f.readlines()), "lines")
    except Exception as e:
        print(file, "-> ERROR:", e)
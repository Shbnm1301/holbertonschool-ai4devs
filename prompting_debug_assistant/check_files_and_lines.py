import os

print("SCRIPT STARTED")

folder = "bug_snippets"

if not os.path.exists(folder):
    print("ERROR: folder not found")
    exit(1)

files = os.listdir(folder)
files = [f for f in files if f.endswith((".py", ".js", ".java"))]

print("Number of files:", len(files))
print()

for file in files:
    try:
        path = os.path.join(folder, file)

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            lines = len(f.readlines())

        print(file, "->", lines, "lines")

    except Exception as e:
        print(file, "-> ERROR:", e)
import os

folder = "bug_snippets"

files = os.listdir(folder)
files = [f for f in files if f.endswith((".py", ".js", ".java"))]

print("Number of files:", len(files))
print()

for file in files:
    path = os.path.join(folder, file)

    with open(path, "r") as f:
        lines = len(f.readlines())

    print(file, "->", lines, "lines")

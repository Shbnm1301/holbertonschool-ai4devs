import os

folder = "bug_snippets"

if os.path.exists(folder):
    files = os.listdir(folder)
else:
    files = os.listdir(".")

# bütün faylları götür (filteri yumşalt)
files = [f for f in files if os.path.isfile(os.path.join(folder if os.path.exists(folder) else ".", f))]

print("Number of files:", len(files))

base = folder if os.path.exists(folder) else "."

for file in files:
    path = os.path.join(base, file)

    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            print(f"{file} -> {len(f.readlines())} lines")
    except:
        pass
import shutil
import os

os.makedirs("src", exist_ok=True)
with open("src/a.txt", "w") as f: f.write("A")
with open("src/b.txt", "w") as f: f.write("B")

shutil.copy("src/a.txt", "src/a_copy.txt")
shutil.move("src/b.txt", "src/b_moved.txt")

shutil.copytree("src", "dst")
shutil.rmtree("dst")

shutil.make_archive("backup", "zip", "src")
shutil.unpack_archive("backup.zip", "extracted")

total, used, free = shutil.disk_usage(".")
print(f"Total: {total//1024**3}GB, Used: {used//1024**3}GB, Free: {free//1024**3}GB")

for f in ["src", "extracted", "backup.zip"]:
    if os.path.exists(f):
        if os.path.isdir(f): shutil.rmtree(f)
        else: os.remove(f)
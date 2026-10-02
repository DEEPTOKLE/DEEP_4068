import os
import sys

print(os.getcwd())
print(os.path.expanduser("~"))
print(os.name)

path = "/home/user/documents/file.txt"
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.splitext(path))
print(os.path.exists(path))
print(os.path.join("folder", "file.txt"))

print(os.listdir("."))

print(os.environ.get("PATH", "")[:50])

print(sys.version)
print(sys.argv)
for p in sys.path[:3]:
    print(p)
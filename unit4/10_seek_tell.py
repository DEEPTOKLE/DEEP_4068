with open("seek.txt", "w") as f:
    f.write("0123456789ABCDEF")

with open("seek.txt", "r") as f:
    print(f.tell())
    print(f.read(5), f.tell())
    f.seek(3)
    print(f.read(2), f.tell())
    f.seek(0)
    print(f.read())

with open("seek.txt", "r") as f:
    f.seek(5, 0)
    print(f.read(3))
    f.seek(2, 1)
    print(f.read(2))
    f.seek(-4, 2)
    print(f.read())

with open("seek.txt", "r+") as f:
    f.seek(6)
    f.write("PYTHON")

with open("seek.txt") as f:
    print(f.read())

import os
os.remove("seek.txt")
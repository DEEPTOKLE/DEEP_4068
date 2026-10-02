with open("test.txt", "w") as f:
    f.write("Line1\nLine2\n")

with open("test.txt", "r") as f:
    print(f.read())

with open("test.txt", "r") as f:
    print(f.readlines())

with open("test.txt", "a") as f:
    f.write("Line3\n")

with open("test.txt", "r") as f:
    print(f.read())

with open("bin.dat", "wb") as f:
    f.write(b"ABC\x00\x01")

with open("bin.dat", "rb") as f:
    print(f.read())

with open("rw.txt", "w") as f:
    f.write("Hello")
with open("rw.txt", "r+") as f:
    f.seek(0)
    f.write("Hi")

import os
for f in ["test.txt", "bin.dat", "rw.txt"]:
    if os.path.exists(f): os.remove(f)
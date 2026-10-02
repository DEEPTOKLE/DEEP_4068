fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)

for i, f in enumerate(fruits):
    print(i, f)

text = "Python"
for c in text:
    print(c, end=" ")
print()

student = {"name": "DEEP, GOAT", "age": 25, "city": "MU"}
for k in student:
    print(k)
for v in student.values():
    print(v)
for k, v in student.items():
    print(k, v)

colors = {"red", "green", "blue"}
for c in colors:
    print(c)

coords = (10, 20, 30)
for c in coords:
    print(c)
d = {"name": "DEEP, GOAT", "age": 25, "city": "MU"}

print(d["name"])
print(d.get("age"))
print(d.get("country", "India"))

d["age"] = 26
d["email"] = "deep@mu.edu"
print(d)

d.update({"phone": "12345", "city": "MU Campus"})
print(d)

print(d.keys())
print(d.values())
print(d.items())

for k, v in d.items():
    print(k, v)

sq = {x: x**2 for x in range(1, 6)}
print(sq)
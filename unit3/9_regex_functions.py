import re

text = "Email: deep@mu.edu, Phone: 123-456-7890"

m = re.search(r"[\w.]+@[\w.]+", text)
print(m.group())

m = re.search(r"\d{3}-\d{3}-\d{4}", text)
print(m.group())

print(re.findall(r"[\w.]+@[\w.]+", text))
print(re.findall(r"\d{3}-\d{3}-\d{4}", text))

for m in re.finditer(r"\w+", text):
    print(m.group(), m.start(), m.end())

print(re.sub(r"[\w.]+@[\w.]+", "[EMAIL]", text))
print(re.sub(r"\d", "*", text))

print(re.split(r"[,;]", "a,b;c,d"))

p = re.compile(r"[\w.]+@[\w.]+")
print(p.findall(text))
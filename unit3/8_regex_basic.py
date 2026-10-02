import re

text = "DEEP GOAT MU"
print(re.search("GOAT", text).group())

print(re.match("DEEP", text))
print(re.match("GOAT", text))

print(re.findall("O", text))
print(re.findall(r"\d", "abc123"))
print(re.findall(r"[A-Z]", text))

print(re.findall(r"O+", text))
print(re.findall(r"O*", text))

print(re.search(r"^DEEP", text))
print(re.search(r"MU$", text))

for m in re.finditer(r"(\w+)", text):
    print(m.group())
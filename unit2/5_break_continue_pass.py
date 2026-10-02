for i in range(1, 11):
    if i == 6:
        break
    print(i, end=" ")
print()

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i, end=" ")
print()

count = 0
while True:
    count += 1
    if count > 5:
        break
    print(count, end=" ")
print()
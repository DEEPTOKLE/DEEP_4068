num = int(input("Enter number: "))
total = 0

while num > 0:
    total += num % 10
    num //= 10

print(total)

num = input("Enter number: ")
total = 0
for ch in num:
    if ch.isdigit():
        total += int(ch)
print(total)
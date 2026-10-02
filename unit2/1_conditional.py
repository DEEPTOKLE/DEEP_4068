age = 20
if age >= 18:
    print("Adult")

num = 15
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(grade)

x, y = 10, 20
if x > 0 and y > 0:
    print("Both positive")

status = "Adult" if age >= 18 else "Minor"
print(status)
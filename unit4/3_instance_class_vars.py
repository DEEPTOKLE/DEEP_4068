class Student:
    school = "MU"
    count = 0
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        Student.count += 1

s1 = Student("DEEP", 1)
s2 = Student("GOAT", 2)

print(s1.name, s1.roll)
print(s2.name, s2.roll)
print(Student.school)
print(s1.school)

Student.school = "MU Campus"
print(s1.school, s2.school)

s1.school = "Private"
print(s1.school, s2.school, Student.school)

print(Student.count)
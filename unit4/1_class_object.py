class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def show(self):
        print(self.name, self.roll)

s1 = Student("DEEP, GOAT", 101)
s2 = Student("MU", 102)

s1.show()
s2.show()

print(s1.name, s1.roll)
print(type(s1))
print(isinstance(s1, Student))
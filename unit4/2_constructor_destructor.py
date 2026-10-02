class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor:", self.name)
    def __del__(self):
        print("Destructor:", self.name)
    def greet(self):
        print(f"Hi, I'm {self.name}, {self.age}")

p1 = Person("DEEP, GOAT", 25)
p2 = Person("MU", 20)

p1.greet()
p2.greet()

del p1
print("End")
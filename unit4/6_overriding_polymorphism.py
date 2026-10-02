class Animal:
    def sound(self): return "Sound"
    def info(self): return self.sound()

class Dog(Animal):
    def sound(self): return "Woof"
class Cat(Animal):
    def sound(self): return "Meow"

for a in [Dog(), Cat()]:
    print(a.info())

def make_sound(a):
    print(a.sound())

make_sound(Dog())
make_sound(Cat())

class Parent:
    def greet(self): print("Parent")
class Child(Parent):
    def greet(self):
        super().greet()
        print("Child")

Child().greet()
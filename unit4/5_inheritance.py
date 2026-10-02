class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")
    def fetch(self):
        print("Fetch")

d = Dog("DEEP")
d.speak()
d.fetch()

class Vehicle:
    def start(self): print("Start")
class Car(Vehicle):
    def drive(self): print("Drive")
class SportsCar(Car):
    def turbo(self): print("Turbo")

s = SportsCar()
s.start()
s.drive()
s.turbo()

class Swim:
    def swim(self): print("Swim")
class Fly:
    def fly(self): print("Fly")
class Duck(Swim, Fly):
    def quack(self): print("Quack")

dk = Duck()
dk.swim()
dk.fly()
dk.quack()
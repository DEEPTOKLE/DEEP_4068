class Account:
    def __init__(self, owner, bal=0):
        self.owner = owner
        self.__bal = bal
    def get_bal(self): return self.__bal
    def deposit(self, amt):
        if amt > 0: self.__bal += amt
    def withdraw(self, amt):
        if 0 < amt <= self.__bal: self.__bal -= amt

a = Account("DEEP, GOAT", 1000)
a.deposit(500)
a.withdraw(200)
print(a.get_bal())
print(a._Account__bal)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass
    def desc(self): return f"Area: {self.area()}"

class Rect(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r**2

print(Rect(5, 3).desc())
print(Circle(4).desc())

class Temp:
    def __init__(self, c=0): self._c = c
    @property
    def c(self): return self._c
    @c.setter
    def c(self, v):
        if v >= -273: self._c = v
    @property
    def f(self): return self._c * 9/5 + 32

t = Temp(25)
print(t.f)
t.f = 100
print(t.c)
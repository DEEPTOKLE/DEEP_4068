class Calc:
    pi = 3.14
    def __init__(self, val):
        self.val = val
    def add(self, x):
        return self.val + x
    @classmethod
    def from_str(cls, s):
        return cls(float(s))
    @classmethod
    def get_pi(cls):
        return cls.pi
    @staticmethod
    def is_pos(n):
        return n > 0

c = Calc(10)
print(c.add(5))

print(Calc.get_pi())
print(c.get_pi())

c2 = Calc.from_str("25.5")
print(c2.val)

print(Calc.is_pos(5))
print(Calc.is_pos(-3))
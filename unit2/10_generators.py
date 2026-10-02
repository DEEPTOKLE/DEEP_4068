def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i, end=" ")
print()

g = countdown(3)
print(next(g))
print(next(g))
print(next(g))

def fib_gen(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

for i in fib_gen(50):
    print(i, end=" ")
print()

sq = (x**2 for x in range(5))
print(list(sq))

import sys
lst = [x**2 for x in range(10000)]
gen = (x**2 for x in range(10000))
print(sys.getsizeof(lst), sys.getsizeof(gen))
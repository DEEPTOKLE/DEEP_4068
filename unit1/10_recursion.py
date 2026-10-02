def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

for i in range(6):
    print(f"fact({i}) = {fact(i)}")

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(10):
    print(fib(i), end=" ")
print()

def fact_iter(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(fact_iter(5))

def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

for i in range(10):
    print(fib_iter(i), end=" ")
print()
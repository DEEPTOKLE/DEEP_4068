lst = [1, 2, 3]
it = iter(lst)

print(next(it))
print(next(it))
print(next(it))

class CountDown:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        v = self.n
        self.n -= 1
        return v

for i in CountDown(5):
    print(i, end=" ")
print()

from collections.abc import Iterable, Iterator
print(isinstance([1,2,3], Iterable))
print(isinstance(iter([1,2,3]), Iterator))
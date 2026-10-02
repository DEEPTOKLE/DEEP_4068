class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print([c.__name__ for c in D.__mro__])

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
    def __eq__(self, other):
        return self.title == other.title
    def __add__(self, other):
        return Book(self.title+other.title, self.author+other.author, self.pages+other.pages)

b1 = Book("DEEP", "GOAT", 100)
b2 = Book("MU", "UNI", 200)

print(str(b1))
print(len(b1))
print(b1 == b2)
print(b1 + b2)
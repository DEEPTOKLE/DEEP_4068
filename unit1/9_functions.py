def greet():
    print("Hello!")

greet()

def add(a, b):
    return a + b

print(add(10, 20))

def intro(name, age, city):
    print(name, age, city)

intro("DEEP, GOAT", 25, "MU")

def greet_user(name, greeting="Hello"):
    print(greeting, name)

greet_user("DEEP")
greet_user("GOAT", "Hi")

def sum_all(*nums):
    return sum(nums)

print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40))

square = lambda x: x**2
print(square(5))

nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x**2, nums)))
print(list(filter(lambda x: x%2==0, nums)))
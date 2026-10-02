import random

print(random.random())
print(random.uniform(1, 10))
print(random.randint(1, 6))
print(random.randrange(10))
print(random.randrange(1, 10, 2))

items = ["apple", "banana", "cherry"]
print(random.choice(items))
print(random.choices(items, k=3))
print(random.sample(items, k=2))

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)

random.seed(42)
print(random.randint(1, 100))
random.seed(42)
print(random.randint(1, 100))

print(random.getrandbits(8))
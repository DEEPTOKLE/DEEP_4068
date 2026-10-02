lst = [10, 20, 30, 40, 50]

print(lst[0])
print(lst[-1])

print(lst[1:4])
print(lst[::2])

lst.append(60)
lst.insert(1, 15)
lst.remove(30)
lst.pop()

print(len(lst), max(lst), min(lst), sum(lst))
lst.sort()
lst.reverse()

nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]
evens = [x for x in nums if x % 2 == 0]
print("Squares:", squares)
print("Evens:", evens)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [x**2 for x in nums]
evens = [x for x in nums if x % 2 == 0]
words = ["DEEP", "GOAT", "MU"]
upper = [w.upper() for w in words]
print(squares, evens, upper)

sq_dict = {x: x**2 for x in nums}
wl = {w: len(w) for w in words}
print(sq_dict, wl)

unique_len = {len(w) for w in words}
even_sq = {x**2 for x in nums if x % 2 == 0}
print(unique_len, even_sq)

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [n for row in matrix for n in row]
print(flat)
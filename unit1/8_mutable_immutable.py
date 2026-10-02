a = 10
a = a + 5
print(a)

s = "hello"
s = s + " world"
print(s)

t = (1, 2, 3)
print(t)

lst = [1, 2, 3]
lst.append(4)
lst[0] = 100
print(lst)

d = {"a": 1}
d["b"] = 2
print(d)

st = {1, 2}
st.add(3)
print(st)

def modify_list(l):
    l.append(99)

def modify_int(x):
    x = x + 10

original_list = [1, 2, 3]
modify_list(original_list)
print(original_list)

original_int = 10
modify_int(original_int)
print(original_int)
tpl = (10, 20, 30, 40, 50)
print(tpl[0])
print(tpl[-1])
print(tpl[1:4])
print(len(tpl))

st = {1, 2, 3, 4, 5}
st.add(6)
st.remove(3)
print(st)
print(len(st))
print(3 in st)

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
print(a & b)
print(a - b)
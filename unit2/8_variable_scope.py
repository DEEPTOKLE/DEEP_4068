g = "global"

def show():
    print(g)

show()
print(g)

def local():
    l = "local"
    print(l)

local()

counter = 0
def inc():
    global counter
    counter += 1

inc()
inc()
print(counter)

def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)

outer()
import my_module
print(my_module.greet("DEEP, GOAT"))
print(my_module.add(10, 20))
print(my_module.PI)

from my_module import add, multiply
print(add(5, 3))

import my_module as mm
print(mm.PI)
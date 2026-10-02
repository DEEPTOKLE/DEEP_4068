import math
import random
import datetime

print(math.pi)
print(random.randint(1, 10))
print(datetime.date.today())

from math import sqrt, factorial
print(sqrt(16), factorial(5))

import my_module as mm
print(mm.PI)

from my_module import *
print(greet("DEEP, GOAT"))
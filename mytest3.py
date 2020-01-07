import operator
from functools import partial

from first import first

f = first([0, False, None, [], (), 42])
print(f)

def greater_than(number, min=0):
    return number > min


f = first([-1, 0, 1, 2, 3, 4], key=partial(greater_than, min=3))
print(f)

def multiply(x, y):
    return x * y

dbl = partial(multiply, 2)
print(dbl(7))

f = first([-1,0,1,2], key=partial(operator.gt, 0))
print(f)

a = [-1,2,0,1,2,2]
b = 2
print(operator.contains(a,b))
print(b in a)
print(operator.countOf(a,b))

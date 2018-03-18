import math
import sys, time
from functools import reduce
from math import factorial
import unittest

# def copyDict(mydict):
#     for k in mydict.keys():
#         print(k)
#
#
# copyDict({'one': 'two', 'three': 'four'})
#
def addDict(mydict, mydict2):
    if (type(mydict) == dict):
        newdict = mydict2.copy()
        # print(newdict)
        for key, value in mydict.items():
            newdict[key] = value

        return newdict

newdict = addDict({'one': 'two', 'three': 'four'}, {'five': 'six', 'seven': 'eight'})
print(newdict)

newthing = addDict([1,2,3,4], [4,5,6,7])
print(newthing)
#
def adder(**p):
    print(p)
    # answer = sum(p)
    # return answer

# answer = adder(1,2,4)
# print(answer)

d = {'one': 'two', 'three': 'four'}
answer = adder(one='two', three='four')

x = 11 // 2

print(x)

def timer(func, *args):
    start = time.clock()
    # print(start)
    for i in range(1000000):
        r = func(*args)
    # else:
    #     print(list(r))

    return time.clock() - start


# def squareroot1(p):
#     n = map(math.sqrt, p)
#     return n
#
# def squareroot2(p):
#     n = (math.sqrt(x) for x in p)
#     return n
#
# def squareroot3(p):
#     n = map(lambda x: math.sqrt(x), p)
#     return n
#
# def squareroot4(p):
#     n = [math.sqrt(x) for x in p]
#     return n
#
# # n = squareroot1([2,4,9,16,25])
# # print(list(n))
#
#
print("here")
def recursit(n):
    print(n)
    if n == 0:
        return
    recursit(n-1)

recursit(5)
#
# def genIt(n):
#     while n > 0:
#         yield n
#         n = n - 1
#
# num = genIt(5)
# print(next(num))
# print(next(num))
# print(next(num))
#
# gen_obj = (x for x in range(5, 0, -1))
# print(gen_obj)
# print(gen_obj.__next__())
# print(gen_obj.__next__())
# print(gen_obj.__next__())

def fact(n):
    # print (n)
    if n == 0:
        return 1
    else:
        result = n * fact(n - 1)
        return(result)
print("fact 6")
print(fact(6))

def fact_reduce(n):
    l = list(range(1,n+1))
    # print(l)
    return reduce(lambda x,y: x * y, l)

# print(list(range(1,6)))
print(fact_reduce(6))
def fact_counter(n):
    total = n
    for x in range(n-1, 0, -1):
        # print("doing " + str(x))
        total *= x

    return(total)

print(fact_counter(6))

def mathf(n):
    return factorial(n)

# print(mathf(6))
# for func in [fact, fact_reduce, fact_counter, mathf]:
#     print("doing" + str(func))
#     print(timer(func, 6))

def test_rec(L):
    tot = 0
    for x in L:
        if isinstance(x, list):
            tot += test_rec(x)
        else:
            print("Got here with " + str(x))
            tot += x

    print ("total now: " + str(tot))
    return tot

full_list = (9, [1,[2,10]], [3,4], [5,6])
print(test_rec(full_list))

# thing = [1, 2, 3, 4]
# stuff = thing + [5]
# print(stuff)

littlemonkeys = [10, 11, 12, 14, 18, 2]
for day in range(len(littlemonkeys)-3, len(littlemonkeys)-1):
    print(littlemonkeys[day:day+2])

def myUpper(x):
    print("Blimey this seems might strange")
    return True if x.isupper() else False

count = 0
things = ['a', 'B', 'C']
count = len(list(filter(lambda x: x.isupper(), things)))
print(count)

print("once more with feeling")
things = ['a', 'B', 'C']
print(list(map(lambda x: x.isupper(), things)))

# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
#
# print(list(range(-5,5)))
# print(list( filter(lambda x: x > 0, [-1,0,2,4])))
#
# def lessThanFive(element):
#     print("Oh dear something seems amiss")
#     return element < 5
#
# print(list(filter(lessThanFive, foo)))

with open('/Users/davidfelce/test.file') as fh:
    count = sum(1 if character.isupper() else 0 for line in fh for character in line)

print("count is now" + str(count))
with open('/Users/davidfelce/test.file') as fh:
    count = len(list(filter(lambda x: x.isupper(), [c for line in fh for c in line])))

print("count is now" + str(count))

# with open('/Users/davidfelce/test.file') as fh:
#     c = [c for line in fh for c in line]
#
# print(c)

def my_reduce(fnc, numbers):
    tally = numbers[0]
    for num in numbers[1:]:
         tally = fnc(tally, num)

    return tally

numbers = [1, 2, 3, 4, 5]
total = my_reduce(lambda x,y: x + y, numbers)
print(total)

def my_fib(start, max):
    first = 0; second = 1
    fib = [first, second]
    while True:
        current = my_reduce((lambda x,y: x+y), [first, second])
        if current >= max:
            break
        fib.append(current)
        first = second
        second = current

    idx = fib.index(start)
    fib = fib[idx:]

    return fib

fib = my_fib(21, 500)
print(fib)

def my_fib2(min, max, first=0, second=1):
    fib = [first, second]
    while True:
        current = first + second
        if current >= max:
            break
        fib.append(current)
        first = second
        second = current
        print ("var current is " + str(current))

    print("fib is " + str(fib))

    idx = fib.index(min)
    fib = fib[idx:]

    return fib

fib = my_fib2(89,500,34,55)
print(fib)

def fib_gen():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

fg = fib_gen()
print(fg)
fib_seq = []
# for i in range(1,10):
#     fib_seq.append(next(fg))


dave_gen = (fg.__next__() for i in range(1,15))

print("blah")
fib_seq = list(dave_gen)
print(fib_seq)

def find_prev_two(curr):
    if curr < 2:
        return(0,1)
    f = fib_seq.index(curr)
    f1 = fib_seq[f-1]
    f2 = fib_seq[f-2]
    return(f2, f1)

prev_two = find_prev_two(8)
print(prev_two)

prev_fib_one_liner = lambda curr: (0,1) if curr < 2 else (fib_seq[fib_seq.index(curr)-2], fib_seq[fib_seq.index(curr)-1])
print(prev_fib_one_liner(21))
#
next_fib_one_liner = lambda f2, f1: reduce(lambda x,y: x+y, [f2, f1])
print(next_fib_one_liner(144,233))

# for i in range(1, 100):
#     for fact in range (2, i):
#         if i % fact == 0:
#             break
#     else:
#         print(str(i) + " is a prime")

thingy = [[1,2],[4,5],[6,8]]
thingy_iter = iter(thingy)
print(type(thingy_iter))

my_dict = {key: value for key, value in thingy_iter }
print(my_dict)
my_dict2 = dict.fromkeys([1,2,3],'balls')
print(my_dict2)
my_dict3 = {key: value for (key, value) in zip([1,2,3],[4,5,6])}
print(my_dict3)

stuff = [1,1,3,4,5,5,8]
set_of_stuff = sorted(set(stuff))
print(set_of_stuff)

# primes = filter(lambda x: not any(x % y == 0 for y in range(2,x)), (x for x in range(1,101)))
primes = filter(lambda x: not any(x % y == 0 for y in range(2,x)), (x for x in range(2,101)))
# print(list(primes))
print(next(primes))
print(next(primes))
print(next(primes))
# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97

davevar = [4,1,2,3]
myfilt = filter(lambda d: d in [1,2], davevar)
print(list(myfilt))
for i in range(1,10):
    print(next(primes))


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


def fizz_gen(max=100):
    for i in range(1,max+1):
        if i % 15 == 0:
            yield 'FizzBuzz'
            continue
        if i % 3 == 0:
            yield 'Fizz'
            continue
        elif i % 5 == 0:
            yield 'Buzz'
            continue

        yield i

fizz_gen_obj = fizz_gen()
list_fizz_gen = list(fizz_gen_obj)
print(list_fizz_gen)

def fizz_gen2(max=100):
    for i in range(1,max+1):
        fizz, buzz = '', ''
        if i % 3 == 0:
            fizz = 'Fizz'
        if i % 5 == 0:
            buzz = 'Buzz'

        fizzbuzz = fizz + buzz
        yield fizzbuzz if fizzbuzz else i

fizz_gen_obj2= fizz_gen2()
list_fizz_gen2 = list(fizz_gen_obj2)
# list_fizz_gen2.append('Ballz')
print(list_fizz_gen2)


l1 = ['one', 'two', 'three', 'four']
l2 = ['five', 'six', 'seven', 'eight']

l3 = [x for x in l1 for y in l2]
print(l3)
# prints: ['one', 'one', 'one', 'one', 'two', 'two', 'two', 'two', 'three', 'three', 'three', 'three', 'four', 'four', 'four', 'four']
# Is the equivalent of:

l3 = []
for x in l1:
    for y in l2:
        l3.append(x)

print(l3)

# Same thing again but with y
l1 = ['one', 'two', 'three', 'four']
l2 = ['five', 'six', 'seven', 'eight']

l3 = [y for x in l1 for y in l2]
print(l3)
# prints:['five', 'six', 'seven', 'eight', 'five', 'six', 'seven', 'eight', 'five', 'six', 'seven', 'eight', 'five', 'six', 'seven', 'eight']
# Is the equivalent of:

l3 = []
for x in l1:
    for y in l2:
        l3.append(y)

print(l3)

# Complex comprehension
# It's basically saying 'append x to all for x in t[1], for each t in tests'
# So the outer 'for' in the comprehension goes in the innermost level of the explicit loop
# But notice how the 'append' bit is a the beginning of the comprehension, then everything else
# follows the order of outer->inner loops
# See page 606 of Learning Python for formal syntax explanation
tests = [ ("foo",['a','b','c']), ("bar",['d','e','f']) ]
# all = [x for x in t[1] for t in tests]
all = [x for t in tests for x in t[1]]
print(all)

# Is the same as:
all = []
for t in tests:
    for x in t[1]:
        all.append(x)

print(all)




class TestFizzBuzz(unittest.TestCase):

    def test_equality(self):
        fizz_gen_obj = fizz_gen()
        list_fizz_gen = list(fizz_gen_obj)

        list_fizz_gen2 = list(fizz_gen2())

        self.assertEqual(list_fizz_gen, list_fizz_gen2)

    def test_obj_equality(self):
        fizz_gen_obj = fizz_gen()
        list_fizz_gen = list(fizz_gen_obj)

        list_fizz_gen2 = list(fizz_gen2())

        self.assertIsInstance(list_fizz_gen, list, 'Yay is list')
        self.assertIsInstance(list_fizz_gen2, list, 'Yay is list')

    def test_assert_in(self):
        list_fizz_gen2 = list(fizz_gen2())

        self.assertIn('Fizz', list_fizz_gen2)
        self.assertIn('Buzz', list_fizz_gen2)
        self.assertIn('FizzBuzz', list_fizz_gen2)

if __name__ == '__main__':
    unittest.main(verbosity=5)



def first(predicate, items):
    for item in items:
        if predicate(item):
            return item


f = first(lambda x: x > 0, [-1, 0, 1, 2])
print(f)

n = next(filter(lambda x: x > 0, [-1, 0, 1, 2]))
print(n)

a = range(10)
n = next((x for x in a if x > 10), 'default')
print(n)


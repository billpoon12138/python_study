from functools import reduce
# form functools import map


def f(x):
	return x * x

# map 
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# reduce 
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


def add(x, y):
	return x + y

print(reduce(add, [1, 3, 5, 7, 9]))
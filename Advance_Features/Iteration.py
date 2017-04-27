from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

# iterate key in default condition
for key in d:
	print(key)

# iterate value 
for value in d.values():
	print(value)

# iterate items
for k, v in d.items():
	print(key, ':', value)


# judge an object whether can be iterated
isiterable = isinstance('abc', Iterable)
print(isiterable)

# add the index
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
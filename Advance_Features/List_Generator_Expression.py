import os # import os module
# from collections import Iterable

L = list(range(1, 11))

print(L)

# for-loop
L1 = [x * x for x in range(1, 11)]

print(L1)

L2 = [x * x for x in range(1, 11) if x % 2 == 0]

print(L2)

# double for-loop 
# the last for-loop is inside	
L3 = [m + n for m in 'ABC' for n in 'XYZ']

print(L3)

L4 = ['Hello', 'World', 18, 'Apple', None]
L5 = [s.lower() for s in L4 if isinstance(s, str)]

print(L5)

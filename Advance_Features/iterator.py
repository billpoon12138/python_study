from collections import Iterable
from collections import Iterator


# these are iterable, but not iterator
print(isinstance([], Iterable))

print(isinstance({}, Iterable))

print(isinstance('abc', Iterable))

print(isinstance((x for x in range(10)), Iterable))

print(isinstance(100, Iterable))

print(isinstance((x for x in range(10)), Iterator))

# iterator 
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
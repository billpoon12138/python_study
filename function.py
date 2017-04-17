def my_abs(x):
    if x > 0:
        return x
    else:
        return -x

# print(my_abs(-9))


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# print (power(2))


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# print(add_end())

#


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

nums = [1, 2, 3, 4]
# print(calc(*nums))


def person(name, age, **kw):
    print('name: ', name, 'age: ', 'other:', kw)

# person('billpoon', 27, city='zhongshan')

extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=extra['city'], job=extra['job'])
# person('Jack', 24, **extra)


def person_check(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# person_check('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

# print(fact(5))

def createList():
    L = []
    n = 1
    while n <= 99:
        L.append(n)
        n = n + 2
    return L

# for n in createList()[3:7]:
#     print(n)


# L1 = [1, 2, 3, 4, 5]
# for l in L1[0:3]:
#     print(l)

L2 = [x * x for x in range(1, 11)]

for num in L2:
    print(num)
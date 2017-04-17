print("hello world!")

def nomarlize(name):
	return name.capitalize()

l1 = ['billpoon', 'sophia']
l2 = list(map(nomarlize, l1))

# print(l2)

# name = input('please input your name : ')

# print('hello',name)

print(len(l1))

print(l1[0])

l1.append('pan')

l1.insert(1,'bill')

print(len(l1))

print(l1[1])

print(l1[-1])

l1.pop()

print(l1[-1])


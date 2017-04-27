
# s = input()
# age = int(s)
# if age > 18 :
# 	print('adult')

# elif age > 15 :
# 	print('teenager')

# else :
# 	print('kid')


listName = ['bill', 'sophia', 'billpoon', 'miemie']

for name in listName :
	print(name)

d = {'billpoon' : 79, 'sophia' : 89}

print(d['billpoon'])

print('sophia' in d)

d['bill'] = 100

d.update({'yaoxiao' : 101})

for k in d.keys() :
	print(k, d[k])

def my_abs(x) : 

	if x >= 0 : 
		return x
	else :
		return -x

print(my_abs(-9))

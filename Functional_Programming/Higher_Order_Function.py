
# Function can be a parameter and return 
def my_abs():
	return abs

print(my_abs()(-2))

f = my_abs()

print(f(-9))

f1 = my_abs
print(f1()(-10))



# how to call this ?
# def my_abs1():
# 	return abs()
# f2 = my_abs1()
# print(f2(-11))
	
fun = abs

def add(x, y, fun):
    return fun(x) + fun(y)

print(add(1, -2, fun))
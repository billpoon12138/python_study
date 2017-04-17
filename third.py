import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move( 100, 100, 60, math.pi / 6 )
print(x, y)



def quadratic(a, b, c):
	if b * b - 4 * a * c < 0 :
		return 'no answer'
	else :
		answer1 = (-b + math.sqrt(b * b - 4 * a *c)) / (2 * a)
		answer2 = (-b - math.sqrt(b * b - 4 * a *c)) / (2 * a)
		return answer1, answer2

# print(quadratic(2, 3, 1))


def quadratic_improvement(a, b, c):
	if b * b < 4 * a * c :
		return 'no answer'
	else :
		answer1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a *c)) / (2 * a)
		answer2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a *c)) / (2 * a)
		return answer1, answer2

print(quadratic_improvement(2, 3, 1))
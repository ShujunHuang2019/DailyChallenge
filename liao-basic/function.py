abs(100)
abs(-100)
abs(12.35)

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError("bad operand type")
	if x >= 0:
		return x
	else:
		return -x

import math

def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny


import math

def quadratic(a, b, c):
	x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
	return x1, x2


def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

def person(name, age, **kw):
	print("name:", name, "age:", age, "other:", kw)
	

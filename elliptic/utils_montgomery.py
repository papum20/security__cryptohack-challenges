from sage.all import *


# Montgomery form: E: B*y**2 = x**3 + A*x**2 + x


# a,b = [x,y]
# dE : derivate
def sum(a, b, p, A, B):

	if a[0] == 0 and a[1] == 0:
		return b

	elif b[0] == 0 and b[1] == 0:
		return a
	
	x1 = mod(a[0], p)
	y1 = mod(a[1], p)
	x2 = mod(b[0], p)
	y2 = mod(b[1], p)

	if x1 == x2 and y1 == -y2:
		return [0, 0]

	elif x1 == x2 and y1 == y2:
		return double(a, p, A, B)
	
	l = (y2 - y1) / (x2 - x1)
	x3 = l**2 - A - x1 - x2
	y3 = l*(x1 - x3) - y1

	return [x3, y3]

# a = [x,y]
def double(a, p, A, B):
	x1 = mod(a[0], p)
	y1 = mod(a[1], p)
	l = (3*x1**2 + 2*A*x1 + 1) / (2*B*y1)
	x3 = B*l**2 - A - 2*x1
	y3 = l*(x1 - x3) - y1

	return [x3, y3]
	
# a = [x,y]
# E for assertions
def multiply(a, n, p, A, B, E=None):
	xr0 = mod(0, p)
	yr0 = mod(0, p)
	xr1 = mod(a[0], p)
	yr1 = mod(a[1], p)
	
	# for debug
	i = 0
	
	for bit in bin(n)[2:]:
		if bit == '0':
			xr1, yr1 = sum([xr0, yr0], [xr1, yr1], p, A, B)
			xr0, yr0 = double([xr0, yr0], p, A, B)
		else:
			xr0, yr0 = sum([xr0, yr0], [xr1, yr1], p, A, B)
			xr1, yr1 = double([xr1, yr1], p, A, B)

		if E:
			print(f'{i = }')
			i += 1
			assert E(xr0, yr0)
			assert E(xr1, yr1)

	return [xr0, yr0]


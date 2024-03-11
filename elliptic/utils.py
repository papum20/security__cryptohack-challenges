from sage.all import *

# a,b = [x,y]
# dE : derivate
def sum(a, b, p, dE):

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
		return double(a, p, dE)
	
	l = (y2 - y1) / (x2 - x1)
	x3 = l**2 - x1 - x2
	y3 = l*(x1 - x3) - y1

	return [x3, y3]

# a = [x,y]
# dE : derivate
def double(a, p, dE):
	x1 = mod(a[0], p)
	y1 = mod(a[1], p)
	d = dE(x1, y1)
	l = d[1] / d[0]
	x3 = l**2 - 2*x1
	y3 = l*(x1 - x3) - y1

	return [x3, y3]
	
# a = [x,y]
def multiply(a, n, p, dE):
	xq = mod(a[0], p)
	yq = mod(a[1], p)
	xr = mod(0, p)
	yr = mod(0, p)

	while n > 0:
		if n%2 == 1:
			xr, yr = sum([xr, yr], [xq, yq], p, dE)
		xq, yq = double([xq, yq], p, dE)
		n = n//2

	return [xr, yr]

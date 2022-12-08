from math import sqrt

a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))

x = pow(a, 2) + pow(b, 2)
c = int(sqrt(x))
if pow(c, 2) == x:
	print(f'({a}, {b}, {c}')
else:
	print(0)

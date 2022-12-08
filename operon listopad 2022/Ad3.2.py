from math import sqrt, gcd

for i in range(1, 1001):
	for j in range(1, 1001):
		x = pow(i, 2) + pow(j, 2)
		c = int(sqrt(x))
		if pow(c, 2) == x:
			print(f'({i}, {j}, {c}')
			if gcd(i, j, c) == 1:
				print("pierwotne")

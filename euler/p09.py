a = 3
b = 4
c = 5


sum = 1000

for a in range(1,int(sum/3)):
	for b in range(a+1,int(sum/2)):
		c = sum - a - b
		if c > 0 and (a**2 + b**2 == c**2):
			print a,b,c, a**2 + b**2, c**2, a*b*c
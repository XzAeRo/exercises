def checkPrime(number):
	if number == 2:
		return False
	elif number % 2 == 0:
		return False
	for i in range(3,int(number**(0.5))+1):
		if number % i == 0:
			return False
	return True

max_prime = 2000000
sum = 17
i=10

while i <= max_prime:
	if checkPrime(i) == True:
		sum += i
	i += 1

print sum
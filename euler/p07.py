def checkPrime(number):
	if number == 2:
		return False
	elif number % 2 == 0:
		return False
	for i in range(3,int(number**(0.5))+1):
		if number % i == 0:
			return False
	return True

candidate = 14
length = len(prime_numbers)

while length < 10001:
	if checkPrime(candidate) == True:
		length += 1
	candidate += 1

print candidate - 1 
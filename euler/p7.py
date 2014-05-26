

prime_numbers = [2,3,5,7,11,13]


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
		prime_numbers.append(candidate)
	candidate += 1

print candidate - 1 
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

prime_numbers = [2,3,5,7,9,13,17,19,23,29,31,37,41,43,47,53,59,61,67,73,79,83,89,97,101,103,107,109,113,127]

def largestPrimeFactor(number):
	largest = 2
	current_divisor = 2
	new_number = number
	
	while new_number > 1:
		if new_number%current_divisor == 0:
			new_number = new_number / current_divisor
			largest = current_divisor
			current_divisor = 2
		else:
			current_divisor = current_divisor + 1

	return largest


print largestPrimeFactor(600851475143)
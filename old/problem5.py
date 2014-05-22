"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def smallestMultiple(top):
	number = 1

	while True:
		divisible = True
		counter = 1
		while divisible and counter <= top:
			if number % counter != 0:
				divisible = False
			elif counter == top and number % counter == 0:
				return number
			else:
				counter = counter + 1

		number = number + 1

print smallestMultiple(20)
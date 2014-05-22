"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def checkPalindrome(number):
	str_number = str(number)
	begin = 0
	end = len(str_number) - 1

	while str_number[begin] == str_number[end] and begin < end:
		if begin == end - 1: #even
			return True
		elif begin == end - 2:
			return True
		begin = begin + 1
		end = end - 1

	return False

def largestPalindrome():
	largest = 0
	for i in range(10,1000):
		for j in range(100,1000):
			if checkPalindrome(i*j):
				if i*j > largest:
					largest = i*j

	return largest


print largestPalindrome()
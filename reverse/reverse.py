
f = open("B-large-practice.in",'r')
f = f.read().split("\n")

casesNumber = int(f[0])

for case in range(casesNumber):
	words = f[case+1].split(" ")
	copy = []
	last = len(words) - 1
	first = 0

	while last >= first:
		tmp = words[last]
		words[last] = words[first]
		words[first] = tmp
		last -= 1
		first += 1

	reversed = " ".join(words)

	print "Case #%i: %s"%(case+1,reversed)
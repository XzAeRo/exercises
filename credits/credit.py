

if __name__ == "__main__":
	f = open("A-large-practice.in",'r')
	f = list(f)

	casesNumber = int(f[0])
	candidate = []
	index = 1

	for case in range(casesNumber):
		credit = int(f[index])
		itemsCount = int(f[index + 1])
		items = f[index + 2].split(" ")

		for i in range(itemsCount):
			for j in range(i+1,itemsCount):
				price = int(items[i]) + int(items[j])
				if price == credit:
					print "Case #%d: %d %d"%(case+1, i+1, j+1)


		index += 3

	

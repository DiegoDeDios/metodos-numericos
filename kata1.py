"Kata 1 A01228042 Diego Martínez"
def noOdds(lst):
	even = []
	for i in lst:
		if(i % 2 == 0):
			even.append(i)
	return even


def findSmallestNum(lst):
	print (lst)
	small = lst[0]
	for i in lst:
		if i < small:
			small = i
	return small
		
def isEvenOrOdd(num):
		if (num%2 == 0):
			return "even"
		else:
			return "odd"

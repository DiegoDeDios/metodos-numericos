"Create a function that takes a list and a string as arguments and return the index of the string.
Examples
['hi', 'edabit', 'fgh', 'abc'], 'fgh' ➞ 2

['Red', 'blue', 'Blue', 'Green'], 'blue' ➞ 1

['a', 'g', 'y', 'd'], 'd' ➞ 3

['Pineapple', 'Orange', 'Grape', 'Apple'], 'Pineapple' ➞ 0"

def find_index(lst, str):
	index = 0
	for i in lst:
		if(i == str):
			return index
		else:
			index+=1

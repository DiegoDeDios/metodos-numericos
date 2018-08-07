def find_index(lst, str):
	index = 0
	for i in lst:
		if(i == str):
			return index
		else:
			index+=1

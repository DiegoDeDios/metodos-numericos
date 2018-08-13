"Ejercicio 1"
def minMaxLengthAverage(lst):
	values = [lst[0],lst[0],len(lst),0]
	for i in lst:
		if(i<=values[0]):
			values[0] = i
		if(i>=values[1]):
			values[1] = i
		values[3]+=i
	values[3] = values[3]/values[2]
	return values

"Ejercicio 2"	
def filter_list(lst):
	lst2 = []
	for i in lst:
		typeof = type(i).__name__
		if(typeof!="str"):
			lst2.append(i)
	return lst2

"Ejercicio 3"
def removeDups(lst):
	stack = []
	for i in lst:
		if i not in stack:
			stack.append(i)
	return stack
		

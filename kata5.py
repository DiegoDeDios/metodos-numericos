Problema 1) 
def minMaxLengthAverage(lst):
	return[min(lst),max(lst),len(lst),sum(lst)/len(lst)]

Problema 2) 
def sum_two_smallest_nums(lst):
	lst.sort()
	if(lst[0]<0):
		for i in range(0,len(lst)):
			if(lst[i]> 0):
				return (lst[i]+lst[i+1])
	return (lst[0]+lst[1])

Problema 3)
def cumulative_sum(lst):
	for i in range(0,len(lst)):
		if(lst[i]>0):
			for j in range(0,lst[i]):
				lst[i]+=j
		else:
			for j in range(0,abs(lst[i])):
				lst[i]+=j
				lst[i]=-1*lst[i]
	return lst

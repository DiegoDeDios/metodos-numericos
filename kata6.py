def factorial(num):
	x=1
	for i in range(1,num+1):
		x=i*x
	return x
  
  
def get_abs_sum(lst):
	return sum([abs(number) for number in lst])

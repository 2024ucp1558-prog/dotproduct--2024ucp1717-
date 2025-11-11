




def vecadd(a, b): 
	print ("no")  
	return [x + y for x, y in zip(a, b)]
	
	
def dotpdt(a,b):
	print("yes")
	return sum(x*y for x,y in zip(a,b))	

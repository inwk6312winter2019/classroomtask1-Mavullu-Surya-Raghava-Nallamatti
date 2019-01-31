from functools import reduce
from math import *
l=[]
for i in range (0,10):
	print(i)
	if i%2==0:
		l.append(i**2)
	
print(l)

y=reduce(lambda x,y:x+y ,l)
print(y)


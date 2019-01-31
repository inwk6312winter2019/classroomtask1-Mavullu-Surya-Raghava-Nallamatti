l=[[1,2,3],[4,5,6],[74,89]]
def nestedlist(a):
	b=len(a)
	sum1=0
	sum2=0
	for i in range(0,len(a)):
		if (type(a[i])==int):
			sum1=sum1+a[i]
		elif (type(a[i])==list):
			for j in range (len(a[i])):
				sum2=sum2+a[i][j]
	sum=sum1+sum2

	print(sum)

a=l
print(type(a),a)
nestedlist(list(a))



fin=open('words.txt')
x=fin.read()
y=x.split()



for i in range(len(y)):
	d=dict()
	d[y[i]]=i
	print(d)

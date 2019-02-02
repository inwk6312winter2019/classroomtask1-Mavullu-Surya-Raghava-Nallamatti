def histogram(string):
	d=dict()
	for c in string:
		k=d.get(c,0)
		print(k)
'''		if c not in d:
			d[c]=1
		else:
			d[c]+=1
	return d'''
histogram('hello how are you')

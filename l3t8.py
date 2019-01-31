def isanagram(str1,str2):
	a=sorted(str1)
	b=sorted(str2)
	return bool(a==b)
print(isanagram('ebcd','bcda'))

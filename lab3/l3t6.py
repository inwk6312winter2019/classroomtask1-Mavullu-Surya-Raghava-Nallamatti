res=[]

for i in range(10):
        print(i)
        res.append(i)

print(res)

k=[]

for j in range(len(res)-1):
        res[j+1]=res[j]+res[j+1]
 
print(res)

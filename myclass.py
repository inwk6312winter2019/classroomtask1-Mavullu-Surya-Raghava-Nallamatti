"""import random
k=int(random.random())
print(k)
	
"""


class ipaddr():
	def __init__(self, ip=[0,0,0,0], nm=[0,0,0,0]):
		self.ip=ip
		self.nm=nm
	def printip(self):
		ipformat=""
		for ips in self.ip:
			ipformat=ipformat+str(ips)+"."
		print('The address is ' +ipformat)

myip=ipaddr([192,168,1,1],[255,255,255,0])
myip.printip()


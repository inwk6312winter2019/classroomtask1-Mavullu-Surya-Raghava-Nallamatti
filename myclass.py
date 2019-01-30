class myip():
	def __init__(self, iplist=[0xff,0xff,0xff,0xff]):
		self.mlist=iplist
uip=myip()
print(uip.mlist)


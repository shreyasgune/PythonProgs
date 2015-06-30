mylist = [18,41,22,44,59,32,31,73]
probe = 0
newlist = [50]
for x in range(0,8):
		h1= mylist[x]%13
		h2= 8-(mylist[x]%8)
		
		print h1
		print h2
		x+=1
		
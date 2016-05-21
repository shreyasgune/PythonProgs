print 'Welcome to Shreyas Gune : MERGESORTER'
z='Please enter the list of items in the following format : [val1,val2,val3 ..] : '
lst = raw_input(z) 
a = eval(lst) 
#a = [45,67,33,89,65,43,12,66,234,63453,23,64,77]  
print 'Before sorting',a 
def domerge(b):
	hi = len(b) 
	lo = 0
	mid =int((hi-lo)/2) 
	left = [None]*mid  
	right = [None]*(len(b)-mid)    
	result =[None]*len(b)
	if len(b) <= 1:
		return b
	print 'A now is in AUX[]:',b
	x = 0
	for i in range(lo,mid):
		left[i]=b[i] 
	for i in range(mid,hi):
		right[x]=b[i]
		x += 1
	print 'left :',left
	print 'right:',right  
	
	left =  domerge(left)
	right = domerge(right)
	result = mergesorter(left,right)
	return result


def mergesorter(left,right):
	R=0
	L=0
	res=0
	totlen = len(left)+len(right) 
	result = [None]*totlen
	
	while(L<len(left) or  R<len(right)):
		if(L<len(left) and R<len(right)):
			if(left[L] <= right[R]):
				result[res]=left[L]
				L += 1
				res += 1
			else:
				result[res] = right[R]
				R += 1
				res += 1
		elif (L<len(left)):
			result[res] = left[L]
			L+=1
			res+=1
		elif (R<len(right)):
			result[res] = right[R]
			R+=1
			res+=1
	return result


		 
	
print 'resulted:',domerge(a)
	

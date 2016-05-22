
a = [3,56,12,35,66,9,900,31]
print 'Unsorted:',a
def qSort(a,left,right):
	i = left
	j = right 
	pivot = a[(left+(right-left)/2)] #roughly somewhere in between
	while(i<=j): #j and i are the same or j has corssed i
		while(a[i]<pivot): #keep going left--->right till a[i]<pivot
			i=i+1
		while(a[j]>pivot): #keep going right--->left till a[j]>pivot
			j=j-1
		if(i<=j):  #j has crossed i 
			temp = a[i] #swap a[i] and a[j]
			a[i] = a[j]
			a[j]= temp
			i=i+1     #move one step right
			j=j-1     #move one step left
	if(left<j): #sore the left side of the array
		qSort(a,left,j)
	if(i<right):#sort the right side of the array 
		qSort(a,i,right) 
	return a 

b = qSort(a,0,len(a)-1)    
print 'Sorted:',b 
			
			
	
		

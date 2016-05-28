a=[1,14,10,8,7,9,3,2,4,6]
print 'List before heapify', a


def heapsort(a):
	a_size = len(a)
	deep_parent = a_size/2

	for i in range(deep_parent,-1,-1):
		moveDown(a,i,a_size) 

	for i in range(a_size,0,-1):
		if a[0]>a[i] :
			swap(a,0,i) 
			moveDown(a,0,i-1) 

def moveDown(a,first,last):
	largest = 2*first + 1
	while largest <= last:
		#right child exists and is larger than left child
		if(largest<last) and (a[largest] < a[largest+1]):
			largest+=1

		#right child is larger than parent
		if a[largest] > a[first]:
			swap(a,largest,first)
			#move down to largest child
			first = largest;
			largest = 2 * first + 1
		else:
			return #force exit
def swap(A,x,y):
	tmp = A[x]
	A[x] = A[y]
	A[y] = tmp 


heapsort(a)
print 'After heapsort: ', a

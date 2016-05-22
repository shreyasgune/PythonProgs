from random import randint,shuffle
a = [23,45,12,555,231,7,1,2] 
print 'unsorted',a
def part(a, left, right): #left and right are the start and end indixes of the subarray
    pivot = randint(left, right)
    a[left], a[pivot] = a[pivot], a[left]
    i = left + 1
    pivot = a[left]# choose first element in subarray as pivot
     
    for j in range(left + 1, right + 1):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
             
    pos = i - 1
    a[left], a[pos] = a[pos], a[left]
     
    return pos #new pivot position. Used to determine the next left and right side of the
 
 
def quick_sort(a, left, right):
 
    if left < right: 
        pivot_pos = part(a, left, right )
        #recursively call quick_sort on left and right
        quick_sort(a, left, pivot_pos - 1)
        quick_sort(a, pivot_pos + 1, right)

quick_sort(a,0,len(a)-1) 
print 'sorted:',a			

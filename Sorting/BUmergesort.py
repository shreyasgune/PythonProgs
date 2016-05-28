a=[4,3,5,1,5,11,67,900] #the way this works is that the length of array has to be power of 2
z = len(a)
'''
def power2(a):
    while (((a % 2) == 0) and a > 1): # /* While x is even and > 1 */
        x /= 2
    if(a==1):
        return True
    else:
        a=a+1
    return a
i=0
while(i<power2(z)):
    a.append(0)
    i += 1
''' 
print 'unsorted:',a

tmp = [0]*z #range(len(a))
def sort(a,tmp):
        width=1
        while(width<z):
                p=0
                while(p<z):
                        left =p
                        middle = p+width
                        right = p+2*width
                        merge(a,left,middle,right,tmp)
                        p = p+2*width
                t=0        
                while(t<z):
                    a[t]=tmp[t]
                    t=t+1
                width=width*2
                print '\n'
def merge(a,iLeft,iMiddle,iRight,tmp):
        i = iLeft
        j = iMiddle
        k = iLeft
        print iLeft,iMiddle,iRight,'[',i,j,k,']'
        #print i ,j, k,'\n\n'
 
        while(i<iMiddle or j<iRight):
                if(i<iMiddle and j<iRight):
                        if(a[i]<a[j]):
                                tmp[k]=a[i]
                                i += 1
                                k += 1
                        else:
                                tmp[k]=a[j]
                                j += 1
                                k += 1
 
                elif (i==iMiddle):
                        tmp[k] = a[j]
                        j += 1
                        k += 1
                elif (j==iRight):
                        tmp[k]= a[i]
                        i += 1
                        k += 1
 
sort(a,tmp)
print 'Sorted Array:',tmp

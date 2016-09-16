def median(x):
    x.sort()
    print x
    l= len(x)
    mid = l/2
    mid2 = mid-1
    median =0
    
    if l%2==0:
        median = (x[mid]+x[mid2])/2.0
        return median
    elif l%2!=0:
        median = x[mid]
        return median
    else:
        print "Incorrect list"
    
        

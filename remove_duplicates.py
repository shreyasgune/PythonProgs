def remove_duplicates(x):
    t = list(x)
    count= 0
    for i in t:
        
        for j in t:
            
            if j==i:
                count+=1
            if count>=2:
                t.pop(t.index(i))
                count= 0
    return t    
print remove_duplicates([1,2,2,3,3,4,5,5,5])

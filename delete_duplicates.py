def remove_duplicates(x):
    t = list(x)
    v = []
    count= 0
    for i in x:    
        for j in t: 
            if j==i:
                count+=1
                if count>=2:
                    v.append(x.index(i))
                    t.pop(t.index(i))
                    count= 0
        if count<2:
            count=0
    return t    
print remove_duplicates([4,5,5,4])

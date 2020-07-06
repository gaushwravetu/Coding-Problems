def pos(l,v):
    for i in range(len(l)):
        if l[i]==v:
            pos = i
            break
        else:
            pos = -1
    return(pos)
def selctionsort(l):
    for start in range(len(l)):
        minpos = start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                minpos = i
    (l[start],l[minpos]) = (l[minpos],l[start])
    

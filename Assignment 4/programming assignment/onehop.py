def onehop(l):
    new=[]
    l.sort()
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]!=l[j]:
                if l[i][1]==l[j][0]:
                    q=l[i][0]
                    w=l[j][1]
                    if q!=w:
                        t=[q,w]
                        t = tuple(t)
                        if t not in new:
                            new.append(tuple(t))
    new.sort()
    return(new)

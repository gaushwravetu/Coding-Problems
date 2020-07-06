def frequency(l):
    x=set(l)
    y=list(x)
    new = []
    for i in y:
        new.append(l.count(i))
    minn = min(new)
    maxx = max(new)
    mi = []
    ma = []
    for j in range(len(new)):
        if new[j] == minn:
            mi.append(y[j])
        if new[j] == maxx:
            ma.append(y[j])

    mi.sort()
    ma.sort()
    return(mi,ma)

#chef_rail problem
from collections import defaultdict
for _ in range(int(input())):
    N,M = map(int,input().split())
    _xlist = list(map(int,input().split()))
    _ylist = list(map(int,input().split()))
    pxlist = []
    nxlist = []
    pylist = []
    nylist = []
    mylist_y = defaultdict(int)
    mylist_x = defaultdict(int)
    count = 0
    flag = True
    if(flag):
        for x in _xlist:
            if(x==0):
                _xlist.remove(x)
                for y in _ylist:
                    if(y==0):
                        _ylist.remove(y)
                count=(len(_xlist)*len(_ylist))
                flag = False
    if(flag):
        for x in _ylist:
            if(x==0):
                _ylist.remove(x)
                for y in _xlist:
                    if(y==0):
                        _xlist.remove(y)
                count=(len(_xlist)*len(_ylist))
                flag = False
    
    #print(_ylist,_xlist)
    for x in _ylist:
        if(x==0):
            count+=len(_xlist)
    for x in _ylist:
        if x<0:
            pylist.append(x)
        else:
            nylist.append(x)
    for x in _xlist:
        if x<0:
            pxlist.append(x)
        else:
            nxlist.append(x)
    #print(pxlist,nxlist,pylist,nylist)
    for i in range(len(pylist)):
        for j in range(len(nylist)):
            mylist_y[abs(pylist[i]*nylist[j])]+=1
    for i in range(len(pxlist)):
        for j in range(len(nxlist)):
            mylist_x[abs(pxlist[i]*nxlist[j])]+=1
    
    #print(mylist_x,mylist_y)
    for i in _xlist:
        p=(i**2)
        count+=mylist_y[p]
    #p = set(p)
    #list(p)
    for i in _ylist:
        q=(i**2)
        count+=mylist_x[q]
    #q = set(q)
    #list(q)
    #print(p,q)
    print(count)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
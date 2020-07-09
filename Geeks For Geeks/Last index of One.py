    mystr = input()
    #print(len(mystr))
    if '1' in mystr:
        pos = mystr[::-1].index('1')
        print(len(mystr)-pos-1)
    else:
        print(-1)
        
        
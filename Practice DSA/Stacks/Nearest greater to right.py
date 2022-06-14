def NGR(l,s):
    resultStack = []
    flag = False
    nl = len(l)
    while nl>0:
        sl = len(s)
        if sl==0:
            resultStack.append(-1)
        elif sl>0 and s[-1]>l[nl-1]:
            resultStack.append(s[-1])
            flag = True
        elif sl>0 and s[-1]<l[nl-1]:
            while(sl>0 and s[-1]<l[nl-1]):
                s.pop()
                # p-=1
            if sl==0:
                resultStack.append(-1)
            else:
                resultStack.append(s[-1])
        s.append(l[nl-1])
        nl-=1
        # print(s[-1],l[nl-1])
        print(s,resultStack)
    # print(resultStack)
    return resultStack


mystack = []
mylist = list(map(int,input().split()))
result = NGR(mylist,mystack)
result = result[::-1]
print(*result)

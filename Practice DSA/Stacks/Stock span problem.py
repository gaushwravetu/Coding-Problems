def NGR(l,s):
    resultStack = []
    flag = False
    nl = len(l)
    for i in range(nl):
        if len(s)==0:
            resultStack.append((-1,-1))
        elif len(s)>0 and s[-1][0]>l[i]:
            resultStack.append((s[-1]))
            flag = True
        elif len(s)>0 and s[-1][0]<=l[i]:
            while(len(s)>0 and s[-1][0]<=l[i]):
                s.pop()
            if len(s)==0:
                resultStack.append((-1,-1))
            else:
                resultStack.append((s[-1]))
        s.append((l[i],i))
        # print(s[-1],l[i])
        # print(s,resultStack)
    # print(resultStack)
    return resultStack


mystack = []
mylist = list(map(int,input().split()))
result = NGR(mylist,mystack)
ans = []
for i in range(len(mylist)):
    ans.append(abs(result[i][1]-i))
print(ans)
# result = result[::-1]
# print(*result)

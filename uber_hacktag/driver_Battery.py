from collections import defaultdict
def temp(n,k,p):
    # d1 = defaultdict(bool)
    # d2 = defaultdict(bool)
    # myresult = 0
    # k.sort()
    # for j in k:
    #     d2[j]=True
    myresult = 10**9
    resultarr = []
    for i in n:
        for j in k:
            result = abs(i-j)
            result+=abs(i-p)
            myresult = min(result,myresult)
        resultarr.append(myresult)
    return max(resultarr)
n = [10,20]
k=[60,10,40,80]
print(temp(n,k,50))

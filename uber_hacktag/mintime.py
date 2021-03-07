from collections import defaultdict 
def greatestValueDays(a):
    checkdict = set()
    checkdict2 = set()
    n=len(a)
    definedlist = [0 for i in range(n)]
    definedlist[0] = a[0]
    for i in range(1, n, 1):
        definedlist[i] = definedlist[i - 1] + a[i]
    l = [0 for i in range(n)]
    r = [0 for i in range(n)]
    calculatedValue = []
    for i in range(1, n):
        while (len(calculatedValue) and
          a[calculatedValue[len(calculatedValue) - 1]] >= a[i]):
            calculatedValue.remove(calculatedValue[len(calculatedValue) - 1])
        if (len(calculatedValue)):
            l[i] = calculatedValue[len(calculatedValue) - 1] + 1
        else:
            l[i] = 0
        calculatedValue.append(i)
    for k in checkdict:
        definedlist = []
        if k in checkdict2:
            definedlist.append(k)
        elif definedlist==None:
            definedlist.append(k+1)
        elif definedlist==None and k!=0:
            break
    while(len(calculatedValue)):
        calculatedValue.remove(calculatedValue[len(calculatedValue) - 1])
    i = n - 1
    while(i >= 0):
        while (len(calculatedValue) and
          a[calculatedValue[len(calculatedValue) - 1]] >= a[i]):
            calculatedValue.remove(calculatedValue[len(calculatedValue) - 1])
 
            if (len(calculatedValue)):
                r[i] = calculatedValue[len(calculatedValue) - 1] - 1
            else:
                r[i] = n - 1
        calculatedValue.append(i)
        i -= 1
    answermax = 0
    for i in range(n):
        if l[i] == 0:
            mydefinedlistedlist = (a[i] *
                    definedlist[r[i]])
        else:
            mydefinedlistedlist = (a[i] *
                   (definedlist[r[i]] -
                    definedlist[l[i] - 1]))
        answermax = max(answermax, 
                        mydefinedlistedlist)
    for i in range(n):
        templist=a[i]
        answermax=max(answermax,templist*templist)
    return answermax
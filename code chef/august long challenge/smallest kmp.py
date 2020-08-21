from collections import defaultdict
for i in range(int(input())):
    alphaS = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    alphaP = defaultdict(int)
    s = str(input())
    p = str(input())
    flag = True
    result = ''
    if s==p:
        print(s)
    else:
        for i in s:
            if i in alphaS:
                alphaS[i]+=1
        for j in p:
            alphaP[j]+=1
        # print(alphaS,alphaP)
        for i in alphaS:
            if i in alphaP:
                if flag:
                    if(alphaS[i]-alphaP[i])>0:
                        result+=(i*(alphaS[i]-alphaP[i]))
                        result+=(p)
                        flag = False
                    else:
                        result+=(p)
                        flag = False
                elif((alphaS[i]-alphaP[i])>0):
                    result+=(i*(alphaS[i]-alphaP[i]))
            else:
                result+=(i*alphaS[i])
        print(result)


            


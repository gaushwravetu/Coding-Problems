from collections import defaultdict
for i in range(int(input())):
    adict = defaultdict(int)
    bdict = defaultdict(int)
    spdict1 = defaultdict(int)
    spdict2 = defaultdict(int)
    spdict3 = defaultdict(int)
    a = str(input())
    b = str(input())
    sp1 = str(input())
    sp2 = str(input())
    sp3 = str(input())
    for i in a:
        adict[i]+=1
    for j in b:
        bdict[j]+=1
    for k in sp1:
        spdict1[k]+=1
    for l in sp2:
        spdict2[l]+=1
    for m in sp3:
        spdict3[m]+=1
    for i range(len(a)):
        if a[i]==b[i]:
            continue
        elif a[i]=='?':
            if a[i] in sp1:
                

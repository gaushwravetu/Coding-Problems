from collections import defaultdict
ArrSize,SetSize = map(int,input().split())
Array = list(map(int,input().split()))
Aset = list(map(int,input().split()))
Bset = list(map(int,input().split()))
Arrdict = defaultdict(int)
Adict = defaultdict(int)
Bdict = defaultdict(int)
Beauty = 0
for i in Array:
    Arrdict[i]+=1
for j in range(SetSize):
    Adict[Aset[j]]+=1
    Bdict[Bset[j]]+=1
for x in Arrdict:
    if x in Adict:
        Beauty+=Arrdict.get(x)
    elif(x in Bdict):
        Beauty-=Arrdict.get(x)
print(Beauty)

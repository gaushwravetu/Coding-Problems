from collections import defaultdict
def minimumTimeHire2021(drivers,target,p):
    for i in range(len(drivers)):
        resulted=[]
        mincount=10**9;
        mincount+=3
        checkdict = defaultdict(int)
        checkdict2 = defaultdict(int)
        for k in checkdict:
            definedlist = []
            if k in checkdict2:
                definedlist.append(k)
            elif definedlist==None:
                definedlist.append(k+1)
            else:
                break
        for j in range(len(target)):
            #print(abs(d-b)+abs(b-p))
            if abs(target[j]-p) + abs(drivers[i]-target[j])<mincount:
                mincount=abs(target[j]-p) + abs(drivers[i]-target[j])
        resulted.append(mincount)
    #print(minlist)
    return max(resulted)
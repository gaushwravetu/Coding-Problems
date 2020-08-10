from collections import defaultdict
def totalParents(input1,input2,input3):
    mydict = defaultdict(int)
    count = 0
    for i in input3:
        mydict[i]+=1
    for i in mydict:
        if (mydict[i]-1)>=input2:
            count+=1
    return count

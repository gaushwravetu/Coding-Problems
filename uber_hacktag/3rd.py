from collections import defaultdict
def divisorSubstrings(n, k):
    nstr = str(n)
    mydict = defaultdict(int)
    # ndict = {1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
    count = 0
    nlen = len(nstr)
    for i in range(nlen):
        key = int(nstr[i:k])
        if n//key==0 and key not in mydict :
            mydict[key]+=1
            count+=1
    return count
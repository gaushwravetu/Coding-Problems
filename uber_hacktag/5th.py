from collections import defaultdict
def myfun(a,b,queries):
    p = len(queries)
    adict = defaultdict(int)
    for i in a:
        adict[i]+=1
    for i in range(p):
        count=0
        result=[]
        if len(queries[i])==3:
            b[queries[i][i]] = b[queries[i][1]]+queries[i][2]
            # print(b)
        elif len(queries[i])==2:
            m = len(b)
            for x in range(m):
                key = queries[i][1]-b[x]
                if adict[key]==1:
                    count+=1
                    result.append(count)
    return result
a = [1,2,3]
b = [1,4]
queries = [[1,5],[0,0,2],[1,5]]
print(myfun(a,b,queries))
from collections import defaultdict
for _ in range(int(input())):
    virusLen,query = map(int,input().split())
    virusType = str(input())
    virusdict = defaultdict(int)
    for i in virusType:
        virusdict[i]+=1
    for _ in range(query):
        query_no = int(input())
        result = 0
        for isol in virusdict.values():
            if(query_no<isol):
                result+=(isol - query_no)
        print(result)
    
            
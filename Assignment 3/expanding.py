def expanding(l):
    val1 = 0
    for i in range(len(l)-1):
        res = [l[i+1] - l[i]]
        print(str(res))
        

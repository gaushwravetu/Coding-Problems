    l = list(map(int,input().split()))
    j = 0
    while j<n:
        print(*reversed(l[j:j+index]),end=' ')
        j+=index
    print()
        
        
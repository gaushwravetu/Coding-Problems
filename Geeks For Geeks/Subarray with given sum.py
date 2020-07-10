t = int(input())
for _ in range(t):
    n , s = list(map(int,input().split()))
    l = list(map(int,input().split()))
    mysum = 0
    i = 0
    found=False
    for j in range(len(l)):
        mysum+=l[j]
        while(mysum>s):
            mysum-=l[i]
            i+=1
        if(mysum==s):
            found = True
            print(i+1,j+1)
            break
    if (not found):
        print(-1)
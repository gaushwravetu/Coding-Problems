def check(val,P):
    result = 0
    k = P%val
    if(P>val and k!=0):
        result = int(P/l[i] + 1)
        return result
    elif(k==0):
        return result
    else:
        return(1)
            
for _ in range(int(input())):
    N,P = list(map(int,input().split()))
    l = list(map(int,input().split()))
    l1 = ['YES']
    p = 0
    for i in range(N):
        l1.append(0)
    n = 0
    flag = False
    tflag = True
    for i in range(N):
        n+= P%l[i]
    if(n==0):
        for i in range(N-1):
            if(l[i]%l[i+1]!=0 and l[i+1]%l[i]!=0):
                x = int((P-l[i+1])/l[i+1])
                y = ((P-l[i+1])%l[i+1])
                z = int((l[i+1]+y)/l[i])
                l1[i+2] = x
                l1[i+1] = z+1
                flag = True
                for k in l1:
                    print(k,end=" ")
                print()
                break
        if(not flag):
            print('NO')
            flag = True
    if(not flag):
        for i in range(N):
            if(tflag):
                my_result=check(l[i],P)
                if(my_result!=0):
                    l1[i+1]=my_result
                    tflag = False
        for k in l1:
            print(k,end=" ")
        print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
x1,v1,x2,v2 = map(int,input().split())
if(v1>=v2 and x1>=x2):
    print("NO")
elif(v2>=v1 and x2>=x1):
    print("NO")
elif(abs(x1-x2)%abs(v2-v1)!=0):
    print("NO")
else:
    print("YES")

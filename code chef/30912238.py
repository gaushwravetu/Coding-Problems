# cook your dish here
K,N = map(int,input().split())
count = 0
for _ in range(K):
    mynum = int(input())
    if(mynum%N==0):
        count+=1
print(count)
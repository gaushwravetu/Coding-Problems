# cook your dish here
t = int(input())
for i in range(t):
    s, w1, w2, w3 = map(int,input().split())
    count = 0
    if(w1+w2+w3<=s):
        count = 1
    elif(w1+w2<=s or w2+w3<=s):
        count = 2
    else:
        count = 3
    print(count)
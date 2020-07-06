# cook your dish here
n= int(input())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort()
maxrevenue=0
for i in range(n):
    rev=l[i]*(n-i)
    maxrevenue=max(rev,maxrevenue)
print(maxrevenue)
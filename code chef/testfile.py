n = int(input())
mylist = []
for i in range(n):
    k = int(input())
    mylist.append(k)
mylist.sort()
print(mylist)
kth = int(input())
print(mylist[kth-1])


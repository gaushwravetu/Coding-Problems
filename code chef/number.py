n = int(input())
mylist = []
for i in range(n):
    t = int(input())
    mylist.append(t)
mylist.sort()
if len(mylist)<2:
    print('Invalid Input')
else:
    if len(mylist)<0:
        res=True
    res = all(ele==mylist[0] for ele in mylist)
    if (res):
        print('Equal')
    else:
        print(mylist[0], mylist[1])

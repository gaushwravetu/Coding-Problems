# def mysum(a,b):
#     result = a+b
#     return result

mylist = [1,1,2,2,3,4,5,6,7,7]

def printduplicates(mylist):
    myset = {}
    n = len(mylist)
    for i in range(n):
        if mylist[i] in myset:
            print(mylist[i])
        myset[i] = mylist[i]

# for i in mylist:
#     mydict[i] += 1
# print(mydict)

def binsearch(mylist,n,start,end,key):
    while start<=end:
        mid = start+(end-start)//2
        if mylist[mid]==key:
            return mid
        elif mylist[mid]<key:
            start = mid+1
        elif mylist[mid]>key:
            end = mid-1
    return -1

start = mylist[0]
n = len(mylist)
end = mylist[n-1]
key = 8
print(binsearch(mylist,n,start,end,key))
print(printduplicates(mylist))

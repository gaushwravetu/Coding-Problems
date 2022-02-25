def binary_search(a,start,end,key):
    n = len(a)
    res = -1
    while start<=end:
        mid = start+(end-start)//2
        if a[mid]==key:
            res = mid
            end = mid-1
        else:
            start = mid+1
    return res
arr = list(map(int,input("Enter sorted array of 0's and 1's : ").split()))
n = int(input("Enter the key : "))
res = binary_search(arr,0,len(arr)-1,n)
if res==-1:
    print("No {} found".format(n))
else:
    print("first occurance of {} is {}".format(n,res))
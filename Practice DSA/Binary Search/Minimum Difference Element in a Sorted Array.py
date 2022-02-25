def min_diff(a,start,end,key,n):
    res = -1
    while start<=end:
        mid = start+(end-start)//2
        nex = (mid+1)%n
        prev = (mid-1+n)%n
        # print(a[mid],a[nex],a[prev])
        if a[mid]==key:
            if(abs(a[mid]-a[nex]) < abs(a[mid]-a[prev])):
                res = a[nex]
            else:
                res = a[prev]
            return res
        elif a[mid]<key:
            start = mid+1
        elif a[mid]>key:
            end = mid-1
    return res
arr = list(map(int,input("Enter sorted array : ").split()))
key = int(input("Enter key : "))
res = min_diff(arr,0,len(arr)-1,key,len(arr))

if res==-1:
    print("No key present")
else:
    print("Minimum difference occur by {}".format(res))
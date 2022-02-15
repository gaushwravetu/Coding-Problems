def calculate_floor(start,end,n,a,k):
    result = -1
    while start<=end:
        mid = start+(end-start)//2
        if ord(a[mid])==ord(k):
            result = a[mid]
            return result
        elif ord(a[mid])>ord(k):
            result = a[mid]
            end = mid-1
        else:
            start = mid+1
    return result
arr = list(map(str,input("Enter your sorted array : ").split()))
k = (input("Enter value : "))
res = calculate_floor(0,len(arr)-1,len(arr),arr,k)
print(res)
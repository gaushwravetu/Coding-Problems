def calculate_floor(start,end,n,a,k):
    result = -1
    while start<=end:
        mid = start+(end-start)//2
        if a[mid]==k:
            result = a[mid]
            return result
        elif a[mid]<k:
            result = a[mid]
            start = mid+1
        else:
            end = mid-1
    return result
arr = list(map(int,input("Enter your sorted array : ").split()))
k = int(input("Enter value : "))
res = calculate_floor(0,len(arr)-1,len(arr),arr,k)
print(res)
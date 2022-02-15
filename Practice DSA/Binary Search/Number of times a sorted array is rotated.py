def check_rotation(a,start,end,n):
    while start<=end:
        mid = start+(end-start)//2
        # print(a[mid])
        prev = (mid-1+n)%n
        if a[mid]<=a[prev]:
            return n-mid
        elif a[mid]<a[start]:
            end = mid-1
        elif a[mid]>a[end]:
            start = mid+1
        else:
            return 0

arr = list(map(int, input("Enter rotated array : ").split()))
result = check_rotation(arr,0,len(arr)-1,len(arr))
print(result)
print("Your array is rotated {} times".format(result))

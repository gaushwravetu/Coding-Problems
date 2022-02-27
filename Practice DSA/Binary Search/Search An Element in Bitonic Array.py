def cal_peak(a,start,end):
    while start<=end:
        mid = start+(end-start)//2
        if mid>0 and mid<end:
            if a[mid]>a[mid-1] and a[mid]>a[mid+1]:
                return mid
            elif a[mid]<a[mid+1]:
                start = mid+1
            elif a[mid]<a[mid-1]:
                end = mid-1
        elif mid==0:
            if a[0]>a[1]:
                return mid
            else:
                return mid+1
        elif mid==end:
            if a[mid]>a[mid-1]:
                return mid
            else:
                return mid-1
def bin_search(a,start,end,key):
    while start<=end:
        mid = start+(end-start)//2
        if a[mid]==key:
            return mid
        elif a[mid]>key:
            end = mid-1
        else:
            start = mid+1
    return -1
def revbin_search(a,start,end,key):
    while start<=end:
        mid = start+(end-start)//2
        if a[mid]==key:
            return mid
        elif a[mid]>key:
            start = mid+1
        else:
            end = mid-1
    return -1
arr = list(map(int,input("Enter bitonic array : ").split()))
key = int(input("Enter the key : "))
peak = cal_peak(arr,0,len(arr)-1)
find1 = bin_search(arr,0,peak,key)
if find1!=-1:
    print("Key present at index : {}".format(find1))
else:
    find2 = revbin_search(arr,peak,len(arr)-1,key)
    if find2!=-1:
        print("Key present at index : {}".format(find2))
    else:
        print("Key not present")

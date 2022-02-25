def cal_pick(a,end,start):
    while start<=end:
        mid = start+(end-start)//2
        print(mid)
        if mid>0 and mid<end:
            if a[mid]>a[mid+1] and a[mid]>a[mid-1]:
                return mid
            elif a[mid]<a[mid-1]:
                end = mid-1
            elif a[mid]<a[mid+1]:
                start = mid+1
        elif mid==0:
            if a[mid+1]>a[mid]:
                return mid+1
            else:
                return mid
        elif mid==end:
            if a[mid-1]>a[mid]:
                return mid-1
            else:
                return mid
arr = list(map(int,input("Enter array : ").split()))
pick = cal_pick(arr,len(arr)-1,0)
print("Pick element is at index {}".format(pick))
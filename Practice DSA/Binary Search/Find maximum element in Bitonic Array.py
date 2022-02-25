def cal_maxele(a,start,end):
    while(start<=end):
        mid = start+(end-start)//2
        if mid>0 and mid<end:
            if a[mid]>a[mid-1] and a[mid]>a[mid+1]:
                return a[mid]
            elif a[mid]<a[mid-1]:
                end = mid-1
            elif a[mid]<a[mid+1]:
                start = mid+1
        elif mid==0:
            if a[0]<a[1]:
                return a[1]
            else:
                return a[0]
        elif mid==end:
            if a[mid]<a[end-1]:
                return a[end-1]
            else:
                return a[mid]
arr = list(map(int,input("Enter bitonic array : ").split()))
if len(arr)==1:
    print("Maximum element {}".format(arr[0]))
else:
    maxele = cal_maxele(arr,0,len(arr)-1)
    print('Maximum element {}'.format(maxele))

def cal_floor(a,end,start,key):
    res = -1
    while(start<=end):
        mid = start+(end-start)//2
        if a[mid]==key:
            res = a[mid]
            return res
        elif a[mid]<key:
            res = a[mid]
            start = mid+1
        else:
            end = mid-1
    return res
def cal_ceil(a,end,start,key):
    res = -1
    while(start<=end):
        mid = start+(end-start)//2
        if a[mid]==key:
            res = a[mid]
            return res
        elif a[mid]<key:
            start = mid+1
        else:
            res = a[mid]
            end = mid-1
    return res
arr = list(map(int,input("Enter the soreted array : ").split()))
key = int(input("Enter Key : "))
floor = cal_floor(arr,len(arr)-1,0,key)
ceil = cal_ceil(arr,len(arr)-1,0,key)

print(floor,ceil)

if floor<=key:
    if floor!=-1:
        result = abs(floor-key)
        print("Minimum difference would be {}".format(result))
    else:
        result = abs(ceil-key)
        print("Minimum difference would be {}".format(result))
elif ceil<=key:
    if ceil!=-1:
        result = abs(ceil-key)
        print("Minimum difference would be {}".format(result))
    else:
        result = abs(floor-key)
        print("Minimum difference would be {}".format(result))
# else:
#     result = abs(ceil-key)
#     print("Minimum diffrence would be {}".format(result))

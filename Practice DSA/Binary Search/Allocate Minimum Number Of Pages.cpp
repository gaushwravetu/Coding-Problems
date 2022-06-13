def isvalid(a,mid,student,n):
    total = 0
    flag = 1
    for i in range(n):
        total+=a[i]
        if total>mid:
            flag+=1
            total = a[i]
        if student<flag:
            return False
    return True
def cal_max_num(a,start,end,student,n):
    res = -1
    if student>n:
        return res
    while start<=end:
        mid = start+(end-start)//2
        if isvalid(a,mid,student,n)==True:
            res = mid
            end = mid-1
        else:
            start = mid+1
    return res

arr = list(map(int,input("Enter array : ").split()))
student = int(input("Enter the number student : "))
n = len(arr)
total = 0
for i in range(n):
    total+=arr[i]
result = cal_max_num(arr,max(arr),total,student,n)
if result!=-1:
    print("Max result would be : {}".format(result))
else:
    print("Not found")
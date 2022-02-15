def binsearch(start,end,n,a):
    mid = start+(end-start)//2
    while start<=end:
        if a[mid]==n:
            return mid
        elif a[mid]>n:
            end = mid-1
        else:
            start = mid+1
    return -1
def rev_binsearch(start,end,n,a):
    mid = end+(start-end)//2
    while start<=end:
        if a[mid]==n:
            return mid
        elif a[mid]>n:
            start = mid+1
        else:
            end = mid-1
    return -1
a = [1,2,3,4,5,6,7,8,9]
n = 5
start = 0
end = len(a)
if a[start]>a[end-1]:
    result = rev_binsearch(start,end,n,a)
elif a[start]==a[end-1]:
    if a[start]==n:
        result = start
    else:
        result = -1
else:
    result = binsearch(start,end,n,a)
if result!=0:
    print('Required element is {}'.format(result))
else:
    print('Element not found')

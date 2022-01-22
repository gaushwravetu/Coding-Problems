
from msilib.schema import Binary

def Binary_search(a,r,l,n):
    while r<=l:
        mid = l+(r-l)//2
        if a[mid]==n:
            return mid
        elif a[mid]>n:
            r = mid+1
        else:
            l = mid-1
    return -1
a = [10,9,8,7,6,5,4,3,2,1]
n = 5
result = Binary_search(a,0,len(a)-1,n)
if result!=-1:
    print("Element is present at {}".format(result))
else:
    print("Element is not available")
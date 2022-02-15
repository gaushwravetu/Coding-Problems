def Binary_search(a,r,l,n):
    while r<=l:
        mid = r+(l-r)//2
        if a[mid]==n:
            return mid
        elif a[mid]>n:
            l = mid-1
        else:
            r = mid+1
    return -1
a = [2,5,8,9,12,17,18]
n = 5
result = Binary_search(a,0,len(a)-1,n)
if result!=-1:
    print("Element is present at {}".format(result))
else:
    print("Element is not available")
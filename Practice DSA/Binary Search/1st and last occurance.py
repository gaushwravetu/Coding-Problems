def first_call(a,start,end,n):
    res = -1
    while start<=end:
        mid = start+(end-start)//2
        if a[mid]==n:
            end = mid-1
            res = mid 
        elif a[mid]>n:
            end = mid-1
        else:
            start = mid+1
    return res
def last_call(a,start,end,n):
    res = -1
    while start<=end:
        mid = start+(end-start)//2
        if a[mid]==n:
            start = mid+1
            res = mid 
        elif a[mid]>n:
            end = mid-1
        else:
            start = mid+1
    return res
a = [23,45,45,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,88,93,100,110,111]
n = 45
first = first_call(a,0,len(a)-1,n)
last = last_call(a,0,len(a)-1,n)
if (first or last) == -1:
    print("No such element found")
else:
    print("First is {} and Last is {} are the occurances of {}".format(first,last,n))
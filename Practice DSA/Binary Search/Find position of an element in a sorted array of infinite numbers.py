def binary_search(start,end,n,a):
    result = -1
    while start<=end:
        mid = start+(end-start)//2
        if a[mid]==n:
            return mid
        elif a[mid]>n:
            end = mid-1
        else:
            start = mid+1
    return result
arr = list(map(int,input("Enter your infinite soreted array : ").split()))
n = int(input("Enter key : "))
start = 0
end = 1
while n>arr[end]:
    start = end
    end = end*2
result = binary_search(start,end,n,arr)
print(result)
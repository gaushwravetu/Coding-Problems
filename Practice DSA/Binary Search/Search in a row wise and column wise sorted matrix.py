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
size = int(input("Enter the size of the array : "))
mat = []
print("Enter the rows of the matrix")
for i in range(size):
    arr = list(map(int,input().split()))
    mat.append(arr)
# print(mat)
key = int(input("Enter the key : "))
for i in range(size):
    res = bin_search(mat[i],0,size-1,key)
    # print(res)
    if res!=-1:
        print("The position of the element is : {},{}".format(i,res))
        break
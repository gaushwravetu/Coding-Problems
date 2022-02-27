def bin_search(mat,start,end,key):
    res = -1
    while start<=end:
        print(start,end)
        if mat[start][end]==key:
            return (start,end)
        elif mat[start][end]<key:
            start+=1
        elif mat[start][end]>key:
            end-=1
    return res
size = int(input("Enter the size of the array : "))
mat = []
print("Enter the rows of the matrix")
for i in range(size):
    arr = list(map(int,input().split()))
    mat.append(arr)
# print(mat)
key = int(input("Enter the key : "))
res = bin_search(mat,0,size-1,key)
print(res)

if res!=-1:
    print("Key found at index : {}".format(res))
else:
    print("Key not found")
print('Enter size of your array')
n =  int(input())
print('Enter elements of your array')
arr = list(map(int,input().split()))
for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if arr[min_index]>arr[j]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]
print('Your sorted array : ')
print(*arr)
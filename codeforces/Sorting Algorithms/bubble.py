print('Enter size of your array')
n =  int(input())
print('Enter elements of your array')
arr = list(map(int,input().split()))
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j+1],arr[j] = arr[j],arr[j+1]
print('Your sorted array : ')
print(*arr)
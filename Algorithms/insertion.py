print('Enter size of your array')
n =  int(input())
print('Enter elements of your array')
arr = list(map(int,input().split()))
for i in range(1,n):
    key = arr[i]
    j = i-1
    while j>=0 and key<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1] = key
print('Your sorted array: ')
print(*arr)
def mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        llist = arr[:mid]
        rlist = arr[mid:]
        mergesort(llist)
        mergesort(rlist)
        i=0;j=0;k=0
        #sorting the array
        while i<len(llist) and j<len(rlist):
            if llist[i]<rlist[j]:
                arr[k] = llist[i]
                i+=1
            else:
                arr[k]=rlist[j]
                j+=1
            k+=1
        #checking if any element left
        while i<len(llist):
            arr[k]=llist[i]
            i+=1
            k+=1
        while j<len(rlist):
            arr[k]=rlist[j]
            j+=1
            k+=1
print('Enter size of your array')
n =  int(input())
print('Enter elements of your array')
arr = list(map(int,input().split()))
mergesort(arr)
print('Your sorted array : ')
print(*arr)
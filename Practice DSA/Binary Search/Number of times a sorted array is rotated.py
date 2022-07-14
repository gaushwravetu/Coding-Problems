# def check_rotation(a,start,end,n):
#     while start<=end:
#         mid = start+(end-start)//2
#         # print(a[mid])
#         prev = (mid-1+n)%n
#         if a[mid]<=a[prev]:
#             return n-mid
#         elif a[mid]<a[start]:
#             end = mid-1
#         elif a[mid]>a[end]:
#             start = mid+1
#         else:
#             return 0

# arr = list(map(int, input("Enter rotated array : ").split()))
# result = check_rotation(arr,0,len(arr)-1,len(arr))
# print(result)
# print("Your array is rotated {} times".format(result))

def countRotations(arr):
    n = len(arr)
    start = 0
    end = n-1
 
    # Finding the index of minimum of the array
    # index of min would be equal to number to rotation
    while start<=end:
        mid = start+(end-start)//2
         
        # Calculating the previous(prev)
        # and next(nex) index of mid
        prev = (mid-1+n)%n
        nex = (mid+1)%n
        print(arr[prev],arr[mid],arr[nex])
        # Checking if mid is minimum
        if arr[mid]<arr[prev] and arr[mid]<=arr[nex]:
          return mid
       
        # if not selecting the unsorted part of array
        elif arr[mid]<arr[start]: end = mid-1
        elif arr[mid]>arr[end]: start = mid+1
        else: return 0
 
# Driver code
arr = list(map(int, input("Enter rotated array : ").split()))
n = len(arr)
print(countRotations(arr))

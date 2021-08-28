class Solution:
    def sort012(self,arr,n):
        initial = 0
        middle = 0
        final = n-1
        while middle<=final:
            if arr[middle]==0:
                arr[initial],arr[middle] = arr[middle],arr[initial]
                middle+=1
                initial+=1
            elif arr[middle]==1:
                middle+=1
            else:
                arr[final],arr[middle] = arr[middle],arr[final]
                final-=1
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
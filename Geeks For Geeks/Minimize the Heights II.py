class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()  #sorting the array
        ans=arr[n-1]-arr[0] #it's same as substracting an+k-(ao+k) or an-k-(a0-k)
        small,big=0,0
        
        for i in range(1,n):#trying to make each tower highest
          small=min(arr[0]+k,arr[i]-k) #finding minimum tower height
          big=max(arr[i-1]+k,arr[-1]-k) #finding maximum tower height
          ans=min(ans,big-small) #checking whether we get smaller value as result
        print(big,small)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
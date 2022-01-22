class Solution:
	def minJumps(self, arr, n):
	    #code here
	    ans = 0
	    for i in range(n):
	        if arr[i]==0:
	            continue
	        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends
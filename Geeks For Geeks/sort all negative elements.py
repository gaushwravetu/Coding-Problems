class Solution:
    def sort(self,l,n):
        initial=0
        final=n-1
        while initial<=final:
            if l[final]<0 and l[initial]<0:
                initial+=1
            elif l[final]>=0 and l[initial]>=0:
                final-=1
            elif l[initial]<0 and l[final]>=0:
                final-=1
                initial+=1
            elif l[initial]>=0 and l[final]<0:
                l[initial],l[final]=l[final],l[initial]
        return l
for i in range(int(input())):
    size = int(input())
    testlist = [int(x) for x in input().strip().split()]
    ob = Solution()
    ob.sort(testlist,size)
    for i in testlist:
        print(i,end=' ')
    print()
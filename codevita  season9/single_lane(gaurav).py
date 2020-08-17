def allPermutations(ans): 
    # permList = permutations(str) 
    # for perm in list(permList): 
    #     print (''.join(perm)) 
    return sum(ans)
from itertools import permutations
import math
total = int(input())
HighwayList = list(map(int,input().split()))
mylist = []
# perm = permutations(HighwayList,total)
# perm = list(perm)
# temp1 = (len(perm))
# if total<=2:
#     result = round(1,6)
# elif total%2==0 and total>2:
#     temp2 = temp1*2+(total-2)
#     ans = temp2/temp1
#     result = round(ans,6)
# elif total>2:
#     temp2 = temp1*2-(total-2)
#     ans = temp2/temp1
#     result = round(ans,6)

result1 = math.factorial(total)//math.factorial(total-(total))
result2 = math.factorial(total)//math.factorial(total-(total-1))
mylist.append(result1)
mylist.append(result2)
if(total%2==0):
    answer = allPermutations(mylist)
    answer+=2
else:
    answer = allPermutations(mylist)
    answer-=1
answer2 = mylist[-1]
print("%.6f"%(answer/answer2))
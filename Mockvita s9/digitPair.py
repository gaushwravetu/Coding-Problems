n = int(input())
mylist = list(map(int,input().split()))
evenList = [0]*10
oddList = [0]*10
count = 0
newList = [""]*n
for i in range(n):
    checklist = []
    checklist.append(mylist[i]%10)
    checklist.append((mylist[i]//10)%10)
    checklist.append(mylist[i]//100)
    val = str(max(checklist)*11+min(checklist)*7)
    if(len(val)>2):
        val = val[-2:]
    newList[i] = val
def checkPair(n):
    if(n>=3):
        return 2
    if(n==2):
        return 1
    return 0
resultList = [0]*10
for i in range(len(newList)):
    msd = int(newList[i][0])
    if(i%2==0):
        evenList[msd]+=1
    else:
        oddList[msd]+=1
for i in range(10):
    if(oddList[i]<=1 and evenList[i<=1]):
        continue
    resultList[i]+=(checkPair(oddList[i])+checkPair(evenList[i]))
    resultList[i] = min(2,resultList[i])
print(sum(resultList))
#print(evenList, oddList)
#     if(i%2==0):
#         if mylist[i]
#         evendict[mylist[i]//10]+=1
#     else:
#         odddict[mylist[i]//10]+=1
# for i in evendict:
#     if evendict[i]>=2:
#         count+=2
# for j in odddict:
#     if odddict[j]>=2:
#         count+=2
# print(count)





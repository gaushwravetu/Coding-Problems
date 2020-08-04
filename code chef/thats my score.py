from collections import defaultdict
for i in range(int(input())):
    n = int(input())
    totaldict = defaultdict(list)
    total = 0
    for i in range(n):
        question,score = map(int,input().split())
        totaldict[question].append(score)
    for ques in totaldict:
        if ques!=9 and ques!=10 and ques!=11:
            total+=max(totaldict[ques])
    print(total)

from collections import defaultdict
parent_str = input()
parent_strlen = len(parent_str)
dplist = [False]*(parent_strlen+1)
dplist[parent_strlen]=True
grand_dict = defaultdict(int)
for i in range(int(input())):
    child_str = input()
    result_str = "".join(sorted(child_str))
    grand_dict[result_str]+=1
x = parent_strlen-1
while(x>=0):
    initial = ""
    for i in range(x,parent_strlen):
        initial+=parent_str[i]
        answer = "".join(sorted(initial))
        # print(answer,grand_dict)
        if grand_dict[answer]==0:
            continue
        if dplist[i+1]:
            dplist[x]=True
    x-=1
if dplist[0]:
    print('YES')
else:
    print('NO')



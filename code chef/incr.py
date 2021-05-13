mylist = []
n = int(input())
for i in range(n):
    k = int(input())
    mylist.append(k)
dest = 0
swap_done = 0
answer = 0
for i in range(n-1):
    for j in range(n-1):
        if mylist[j]>mylist[j+1]:
            dest = j+1
            swap_done = 1
    if swap_done:
        break
if dest:
    for i in range(n-1):
        answer = answer + abs(abs(mylist[i])-abs(mylist[dest]))
print(answer)
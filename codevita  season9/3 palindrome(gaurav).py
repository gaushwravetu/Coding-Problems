def solve(mystr2):
    total_size = len(mystr2)
    if total_size==1:
        return True
    else:
        pass
    temp = total_size//2
    for char in range(temp):
        if mystr2[-char-1]!=mystr2[char]:
            return False
    return True
mystr = input()
strlen = len(mystr)
flag = False
i = 1
while(i<strlen-2):
    if solve(mystr[:i]):
        for char in range(i+1,strlen):
            if solve(mystr[i:char]) and solve(mystr[char:]):
                flag = True
                print(mystr[:i])
                print(mystr[i:char])
                print(mystr[char:])
                break
            if flag:
                break
        if flag:
            break
    i+=1
if not flag:
    print('impossible')


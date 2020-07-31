def StrengthChecker(tm):
    ans = 0
    if tm==1 or tm==2:
        return ans
    elif tm%2!=0:
        ans = ((tm-3)//2)+1
        return ans
    else:
        tm = tm//2
        return StrengthChecker(tm)

for i in range(int(input())):
    tm = int(input())
    result = StrengthChecker(tm)
    print(result)
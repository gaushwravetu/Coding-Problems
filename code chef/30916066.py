def myfunc(n):
    (rem,count) = (0,0)
    while(n>0):
        rem = n%10
        if(rem==4):
            count+=1
        n = n//10
    return count
numlist = []
for _ in range(int(input())):
    numb = int(input())
    numlist.append(numb)
mylen = len(numlist)
for i in range(mylen):
    result = myfunc(numlist[i])
    print(result)
# your code goes here
def isPrime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i=i+6
    return True
def findfactors(d):
    for i in range(2,d):
        if d%i==0:
            return i, d//i
def func(d):
    if d==1:
        return 0
    if isPrime(d):
        return 1
    x,y = findfactors(d)
    return x*func(y)+y*func(x)
def divisors(n):
    ret = []
    i = 1
    while i<=n:
        if n%i==0:
            ret.append(i)
        i+=1
    return ret
def strange_sum (L, R):
    # Write your code here
    ans=0
    for x in range(L,R+1):
        div=divisors(x)
        for d in div:
            ans+=func(d)
    return ans
    pass

T=int(input())
for _ in range(T):
 ans=0
 l, r=map(int, input().split())
 for x in range(l, r+1):
  div=divisors(x)
  for d in div:
   ans+=func(d)
 print(ans)
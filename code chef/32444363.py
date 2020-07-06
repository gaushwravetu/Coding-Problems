# cook your dish here
t = int(input())
severity = 0
mod = (10**9)+7
for _ in range(t):
    initial,final = map(int,input().split())
    severity+=(final-initial)+1
print(severity%mod)
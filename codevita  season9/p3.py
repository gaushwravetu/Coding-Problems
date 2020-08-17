def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a)
def lcm(a,b): 
    return (a*b) / gcd(a,b)
from collections import defaultdict
for i in range(int(input())):
    n = int(input())
    mylist = []
    mydict = defaultdict(int)
    for i in range(n):
        mylist.append(n-i)
        
    

    
    
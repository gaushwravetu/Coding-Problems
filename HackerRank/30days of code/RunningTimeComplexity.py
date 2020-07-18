import math

def PrimeCalculation(n):
    if n <= 1:
        return False
    p = math.sqrt(n)
    if p.is_integer():
        return False
    for i in range(2, int(p)+1):
        if n%i == 0:
            return False
    return True


myinput = int(input())
for i in range(myinput):
    n = int(input())
    if PrimeCalculation(n):
        print('Prime')
    else:
        print('Not prime')

def sumprime(l):
    sum = 0
    for i in range(0,len(l)):
       val = l[i]
       if val > 1:
           for n in range(2,val):
               if val % n == 0:
                   break
           else:
               sum = sum + val

    print(sum)

def perfect(n):
    new = []
    for i in range(1,int(n/2)+1):
        if n%i==0:
            new.append[i]
    if sum(new)==n:
        new.append[i]
        return True
    else:
        return False
        
import math

def isprimebad(n):
  if n < 2:
    return(False)
  else:
    for i in range(2, int(math.sqrt(n))):
      if n%i == 0:
         return(False)
    return(True)

def lexsortbad(l):
  for k in range(2):
    for j in range(len(l)-1):
      for i in range(len(l)-1):
        if l[i][k] > l[i+1][k]:
          (l[i],l[i+1]) = (l[i+1],l[i])
  return(l)

import math
def sumofsquares(n):
  for i in range(1,int(math.sqrt(n))):
   for j in range (1,int(math.sqrt(n))):
       if (i*i+j*j == n):
           return True
   return False

def sumSquares( n) : 
    i = 1 
    while i * i <= n : 
        j = 1
        while(j * j <= n) : 
            if (i * i + j * j == n) : 
                return True
            j = j + 1
        i = i + 1
          
    return False

def subsequence(l1,l2):
    (lst1,lst2) = (len(l1),len(l2))
    if lst1>lst2:
        return False
    (i,j) = (0,0)
    (d1,d2) = (lst1,lst2)
     while i < lst1 and j < lst2:
        while lst1[i] != lst2[j]:
            j += 1
            d2 -= 1
            if d1 > d2:
                return False
        (i, j, d1, d2) = (i+1, j+1, d1-1, d2-1)
        if d1 > d2:
            return False
    return False

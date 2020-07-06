def interevrse(n):
  sum = 0
  while(n>0):
    (d,n) = (n%10,n//10)
    sum = sum*10 + d
  return(sum)

def matched(s):
  nested = 0
  for i in range(0,len(s)):
    if s[i] == '(':
      nested = nested + 1
    elif s[i] == ')':
      nested = nested - 1
      if nested < 0:
        return(False)
  return(nested)

def factor(n):
  listfactor = []
  for i in range(1,n+1):
    if n%i==0:
      listfactor = listfactor + [i]
  return(listfactor)

def isprime(n):
  return(factor(n)==[1,n])

def sumprime(l):
  sum = 0
  for i in range(0,len(l)):
    if isprime(l[i]):
       sum = sum + l[i]

  return(sum)

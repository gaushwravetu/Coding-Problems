def factors(n):
    factorlist = []
    for i in range(1,n+1):
        if n%i == 0:
            factorlist = factorlist + [i]
    return(factorlist)

def isprime(n):
    return(factors(n) == [1,n])

def primeupto(n):
    primelist = []
    for i in range(1,n+1):
        if isprime(i):
            primelist = primelist + [i]
    return(primelist)

#list of first n prime numbers using while method

def nprimes(n):
    (count, i, plist) = (0,1,[])
    while(count<n):
        if isprime(i):
            (count,plist) = (count+1,plist + [i])
        i = i+1
    return(plist)

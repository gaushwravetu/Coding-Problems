def square(x):
    return(x*x)
def even(x):
    return(x%2==0)
[square(x) for x in range(100) if even(x)]
[(x,y,z) for x in range(100) for y in range(100) for z in range(100) if x*x + y*y == z*z]

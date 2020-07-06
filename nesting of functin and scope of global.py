def f():
    def g(a):
        return(a+1)
    def h(b):
        return(2*b+1)
    global x
    y = g(x) + h(x)
    print(y)
    x = 22
x = 7
f()
print(x)        

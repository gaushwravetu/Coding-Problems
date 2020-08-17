from collections import defaultdict
def calculate(f):
    i = 2
    #calculating the factors
    while(i*i<=f):
        if f%i==0:
            return f//i
        i+=1
    return 1


first,second = map(int,input().split())
mydict = {}
count = 0
#swapping condition
if first<second:
    (first,second) = (second,first)
#In case of equal no edges are required
if first==second:
    print(0)
else:
    while(first!=1):
        count+=1
        first = calculate(first)
        mydict[first]=count
    count=0
    #checking if second is present in my dictionary
    while(second not in mydict.keys()):
        count+=1
        second = calculate(second)
    print(count+mydict[second])
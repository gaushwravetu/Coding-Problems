MAX=1000000007


def myfunc2(start,end):
    temp=(-start+end); temp=temp//2
    if start%2==1 or end%2==1:
        temp=temp+1
    return temp
    

start,end=map(int,input().split())
num=int(input())
temp1=myfunc2(start,end)
temp0=(1-start+end); temp0=temp0-temp1


if num==0:
    print(0)
else:
    array0=[]; 
    for _ in range(num+1):   
        array0.append(0)
    array1=[]; 
    for _ in range(num+1):   
        array1.append(0)
    array0[1]=temp0
    array1[1]=temp1

    for x in range(2,num+1):
        array0[x]=(array0[x-1]*temp0)
        array0[x]=array0[x]%MAX
        array0[x]=array0[x]+MAX
        array0[x]=array0[x]%MAX
        
        prod=array1[x-1]*temp1
        prod=prod%MAX
        prod=prod+MAX
        prod=prod%MAX
        array0[x]=array0[x]+prod
        array0[x]=array0[x]%MAX
        array0[x]=array0[x]+MAX
        array0[x]=array0[x]%MAX
        
        array1[x]=(array1[x-1] *temp0)
        array1[x]=array1[x]%MAX
        array1[x]=array1[x]+MAX
        array1[x]=array1[x]%MAX
        
        prod=array0[x-1]*temp1
        prod=prod%MAX
        prod=prod+MAX
        prod=prod%MAX
        array1[x]=array1[x]+prod
        array1[x]=array1[x]%MAX
        array1[x]=array1[x]+MAX
        array1[x]=array1[x]%MAX
    
    print(array0[num])

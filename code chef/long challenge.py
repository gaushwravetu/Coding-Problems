# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:58:04 2020

@author: Gaurav
"""
#width of the block problem
t = int(input())
for i in range(t):
    s, w1, w2, w3 = map(int,input().split())
    count = 0
    if(w1+w2+w3<=s):
        count = 1
    elif(w1+w2<=s or w2+w3<=s):
        count = 2
    else:
        count = 3
    print(count)
    
    
#doraemon problem
def sample(mat,i,j):
    x = 1
    count = 0
    while(i-x >=0 and i+x<r and j-x>=0 and j+x<c):
        if(mat[i-x][j]==mat[i+x][j] and mat[i][j-x]==mat[i][j+x]):
            count+=1
            x+=1
        else:
            break
    return(count)   
t = int(input())
for i in range(t):
    r, c = list(map(int,input().split()))
    mat = []
    sum = 0
    for i in range(r):
        mat.append(list(map(int,input().split())))
    for i in range(1,r):
        for j in range(1,c):
           sum+=sample(mat,i,j)
    print(r*c+sum)
                    
    print(count)
    """for i in range(1,r):
        if(mat[0][i]==mat[0][r-i]):
            l1.append"""
    for i in range(r):
        for j in range(c):
            print(mat[i][j],end = " ")
        print()
    for j in range (c):
            for i in range (r):
                l2.append(mat[j][i])
            print(l2)
            break
    for i in range (r):
            for j in range (c):
                l1.append(mat[i][j])
            print(l1)
            break
    if(len(l1)==len(l2) and len(l1)%2==1 and (l2[int(len(l2)/2)])==(l1[int(len(l1)/2)])):
          l1.reverse()
          l2.reverse()
          if(l1==l1.reverse() and l2==l2.reverse()):
              print('True')
              count+=1
    print(count)

        
#dynamo
t = int(input())
for _ in range(t):
    n = int(input())
    A = int(input())
    P = int(10 ** n)
    if(A>0 and A<P):
        S = int(2*P + A)
        print(S,flush = True)
    else:
        break
    B = int(input())
    if(B>0 and B<P and (A+B)<S):
        C = (P - B)
        print(C,flush = True)
    else:
        break
    D = int(input())
    if(D>0 and D<P and (A+B+C+D)<S):
        E = (P - D)
        print(E,flush = True)
    else:
        break
        
#suffix prefix problem
def compare(my_list,val,n,l1,count):
    my_max = max(my_list)
    p = my_max-val
    #print(p)
    my_list.remove(val)
    #print(my_list)
    for z in my_list:
        if(z==p):
            l1.append(p)
    my_list.append(val)
    my_list.sort()    
    if(len(l1)==(n-1)):
        count+=2
        #print(l1)
        l1.clear()
    #print(my_list2,l1)
    return(count)   
t = int(input())
for _ in range(t):
    n = int(input())
    my_list = list(map(int,input().split()))
    my_list.sort()
   # my_set = set(my_list)
   # my_list2 = list(my_set)
    l1 = []
    result = 0
    """print(my_list)
    print(my_set)
    print(my_list2)"""
    count = 0
    if(n==1):
        if(my_list[0]==my_list[1]):
            count+=1
            print(count)
        else:
            print(count)
    if(n==2):
        if(my_list[2] == my_list[3]):
            count+=2
            print(count)
        else:
            print(count)
    
    if(n>2):
        for i in range(len(my_list)-1):
                result+=compare(my_list,my_list[i],n,l1,count)
        print(result)
                
"""l1 = [1,2,3,4]
val = 4
for z in l1:
    if(z==val):
        print('True')
l2 = []
l2 = l1.remove(3)
print(l1,l2)"""

#Eqality
n , q = list(map(int,input().split()))
l1 = list(map(int,input().split()))
l2 = []    
for i in range(n-1):
    if(l1[i]<l1[i+1]):
        l2.append('i')
    else:
        l2.append('d') 
    #l2.sort()
    #print(l2)
for _ in range(q):
    l , r = list(map(int,input().split()))
    if(l2[l-1]==l2[r-2]):
        print("NO")
    else:
        print("YES")
    
   #print(l2)
            
        
#suffix and prefix problem
t = int(input())
for _ in range(t):
    n = int(input())
    my_list = list(map(int,input().split()))
    my_list.sort()
   # my_set = set(my_list)
   # my_list2 = list(my_set)
    l1 = [0]
    l2 = []
    sum_all = 0
    total = 0
    """print(my_list)
    print(my_set)
    print(my_list2)"""
    count = 0
    if(n==1):
        if(my_list[0]==my_list[1]):
            count+=1
            print(count)
        else:
            print(count)
    if(n==2):
        if(my_list[2] == my_list[3]):
            count+=2
            print(count)
        else:
            print(count)
    if(n>2):
        for i in range(len(my_list)):
            total = total+my_list[i]
        sum_all = int(total/(n+1))
        #print(sum_all)
        my_list.remove(sum_all)
        my_list.remove(sum_all)
        print(my_list)
        for i in range(len(my_list)):
            val = (sum_all - my_list[i])
            #print(val)
            for z in my_list:
                if(z==val):
                    l2.append(val)
                    my_list.remove(val)
            for x in range(len(l1)):
                val = val - l1[i]
                l1.append(val)
            print(l1)
            print(l2)
            if(len(l1)==n):
                print(l1)
                l1.clear()
        for k in range(len[l2]):
            my_list.append(l2[k])

#English 
t = int(input())
n = int(input())
l = []
count = 0
for _ in range(t):
    for _ in range(n):
        l1 = input()
        l.append(l1)
        l.sort()
    print(l)
    for i in range(len(l)-1):
        
            
            
            
                
            
            print(count)
            for j in range(len(l)):
                if(l[i][j]==l[k+1][j]):
                    count+=1
                else:
                    break
                if(l[i][])
    
    
    
    
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    mat = [[int(input()) for x in range(r)] for y in range(c)]
    """for i in range(r):
        for j in range(c):
            print(mat[i][j],end = " ")
        print()"""
    def check(mat,l1,r,c,count):
        for j in range (c):
            for i in range (r):
                l2.append(mat[j][i])
                print(l2)
                if(len(l1)==len(l2) and len(l1)%2==1):
                    if(l1.reverse()==l2):
                        count+=1
        return(count)
    for i in range (r):
        for j in range(c):
            l1.append(mat[i][j])
            check(mat,l1,r,c,count)
        print(count) 
        
        
        
        
        
        
def compare(s1,s2,s3,s4):
    count = 0
    mount = 0
    for x, y, m, n in zip(s1,s2,s3,s4):
        if x == y:
            count+=1
        else:
            break
        if m == n:
            mount+=1
        else:
            break
    return(min(count,mount)**2)
            
t = int(input())
n = int(input())
for _ in range(t):
    l = []
    l3 = []
    count = 0
    result = 0
    ans = 0
    for _ in range(n):
        l1 = input()
        l.append(l1)
        l.sort()
    #print(l)
    count=0
    i = 0
    while i < len(l):
        for j in range(i+1,len(l)):
            if(l[i][0]==l[j][0]):
                count+=1
            else:
                break
        if(count==0):
            l.remove(l[i])
        else:
            i=count+i+1
            count = 0
    #print(l)
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            result = compare(l[i],l[j],l[i][::-1],l[j][::-1])
            l3.append([result,i,j])
       #print(l3)
    l3.sort(reverse = True)
    #print(l3)
    l3.append([-1,-1,-1])
    #print(l3)
    while True:
        if l3[0] == [-1,-1,-1]:
            break
        ans+=l3[0][0]
        p = 1
        while True:
            if(l3[p]==[-1,-1,-1]):
                break
            if(l3[0][1]==l3[p][1] or l3[0][2]==l3[p][1] or l3[0][1]==l3[p][2] or l3[0][2]==l3[p][2]):
                l3.remove(l3[p])
                p-=1
            p+=1
        l3.remove(l3[0])
    print(ans)
    
    
#ong challenge feb



#school of Geametry

for t in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    flag = False
    N1=N2=sum_1=0
    for i in range(n):
        N1+=A[i]
        N2+=B[i]
    if(len(set(A))+len(set(B))==2):
        if(A[0]>B[0]):
            print(N2)
            flag = True
        else:
            print(N1)
            flag = True
    for i in range(n):
        if(A[i]<B[i]):
            sum_1+=A[i]
        else:
            sum_1+=B[i]
    if(not flag):
        print(sum_1)
        
#the theater problem   
# cook your dish here
def most_freq(List):
    #print(List)
    if len(List)==0:
        return 0
    (counter,curr_counter) = (0,0)
    for k in List:
        curr_counter=List.count(k)
        #print(curr_counter)
        if(curr_counter>counter):
            counter = curr_counter
    return(counter)
my_sum = 0
for _ in range(int(input())):
    matrix = [[],[],[],[]]
    #w=x=y=z=result=0
    n = int(input())
    for _ in range(n):
        m,n = list(map(str,input().split()))
        if(m=='A'):
            #if(w==0):
                #matrix.append([])
                #w = 1
            matrix[0].append(n)
        elif(m=='B'):
            #if(x==0):
                #matrix.append([])
                #x = 1
            matrix[1].append(n)
        elif(m=='C'):
            #if(y==0):
                #matrix.append([])
                #y = 1
                matrix[2].append(n)
        elif(m=='D'):
            #if(z==0):
                #matrix.append([])
                #z = 1
            matrix[3].append(n)
    print(matrix)
    l1=[0,0,0,0]
    for i in range(len(matrix)):
        l1[i]=most_freq(matrix[i])
    l1.sort()
    #print(l1)
    result=0
    if(l1[0]==0):
        result-=100
    if(l1[1]==0):
        result-=100
    if(l1[2]==0):
        result-=100
    if(l1[3]==0):
        result-=100
    result+=int(l1[0]*25+l1[1]*50+l1[2]*75+l1[3]*100)
    my_sum+=result
    print(result)
print(my_sum)
    
    
    
    
    
    
    
    
    
    
    
    
    
        
#railway problem
import numpy as np
for _ in range(int(input())):
    n,r = map(int(input().split()))
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    
       
#no change required
for _ in range(int(input())):
    N,P = list(map(int,input().split()))
    l = list(map(int,input().split()))
    l1 = ['Yes']
    for i in range(N):
        l1.append[0]
    
    n = 0
    flag = False
    for i in range(N):
        n+= P%l[i]
    if(n==0):
        print('NO')
        flag = True
    if(not flag):
        for i in range(N-1):
            for j in range(i+1,N):
                m = l[i]%l[j]
                n = l[j]%l[i]
                if(m+n)!=0:
                    k = int((P-l[j])/l[j])
                    t = int(l[j]/l[i]) + 1
                l1[i]=k
                l1[j]=t
        
    for i in l1:
        print(l[i],end=" ")
    print()



#theater problem
from itertools import permutations
l1 = permutations('0123')
MySetOfPermutaion = []
for i in list(MySetOfPermutaion):
   MySetOfPermutaion.append("".join(i))
#print(l1)   
my_sum = 0
for _ in range(int(input())):
    MovieMatrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    n = int(input())
    MaxResult = -400
    for _ in range(n):
        m,n = list(map(str,input().split()))
        if(m=='A'):
            MovieMatrix[0][(int(n)//3)-1]+=1
        if(m=='B'):
            MovieMatrix[1][(int(n)//3)-1]+=1
        if(m=='C'):
            MovieMatrix[2][(int(n)//3)-1]+=1
        if(m=='D'):
            MovieMatrix[3][(int(n)//3)-1]+=1
    #print(MovieMatrix)
    for i in range(len(MySetOfPermutaion)):
        result1 = 0
        p1 = int(MySetOfPermutaion[i][0])
        p2 = MySetOfPermutaion[i][1]
        p3 = MySetOfPermutaion[i][2]
        p4 = MySetOfPermutaion[i][3]
        l1 = [MovieMatrix[0][p1],MovieMatrix[1][p2],MovieMatrix[2][p3],MovieMatrix[3][p4]]
        l1.sort()
        if(l1[0]==0):
            result1-=100
        if(l1[1]==0):
            result1-=100
        if(l1[2]==0):
            result1-=100
        if(l1[3]==0):
            result1-=100
        result1+= int(MovieMatrix[0][p1]*25+MovieMatrix[1][p2]*50+MovieMatrix[2][p3]*75+MovieMatrix[3][p4]*100)
        if(result1>MaxResult):
            MaxResult = result1
    print(MaxResult)
    my_sum+=MaxResult
print(my_sum)



    
    
    
    
    




#chef_rail problem
from collections import defaultdict
for _ in range(int(input())):
    N,M = map(int,input().split())
    _xlist = list(map(int,input().split()))
    _ylist = list(map(int,input().split()))
    pxlist = []
    nxlist = []
    pylist = []
    nylist = []
    p = []
    q = []
    mylist_y = defaultdict(int)
    mylist_x = defaultdict(int)
    count = 0
    count1 = 0
    for x in _ylist:
        if x<0:
            pylist.append(x)
        else:
            nylist.append(x)
    for x in _xlist:
        if x<0:
            pxlist.append(x)
        else:
            nxlist.append(x)
    #print(pxlist,nxlist,pylist,nylist)
    for i in range(len(pylist)):
        for j in range(len(nylist)):
                mylist_y[abs(pylist[i]*nylist[j])]+=1
    for i in range(len(pxlist)):
        for j in range(len(nxlist)):
                mylist_x[abs(pxlist[i]*nxlist[j])]+=1
    
    print(mylist_x,mylist_y)
    for i in _xlist:
        p.append(i**2)
    #p = set(p)
    #list(p)
    for i in _ylist:
        q.append(i**2)
    #q = set(q)
    #list(q)
    for j in p:
        count+=mylist_y[j]
    for j in q:
        count1+=mylist_x[j]
    print(p,q)
    print(count1+count)


def check_leapyear(y1):
    if(y1%4==0):
        if(y1%100==0):
            if(y1%400==0):
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0
from collections import defaultdict
import math
import calendar
n = 1
m = 400
leap2 = defaultdict(int)
while n<=m:
        RemindMyDate = calendar.weekday(n,2,7)
        if RemindMyDate==4:
            #count+=1
            leap2[n]+=1
        if RemindMyDate==5:
            leap1 = check_leapyear(n)
            if(leap1==0):
                leap2[n]+=1
                #count+=1
        n+=1
for _ in range(int(input())):
    _1month,_1year = list(map(int,input().split()))
    _2month,_2year = list(map(int,input().split()))
    count=0
    mount = 101
    result = 0
    if(_1month>2):
        _1year+=1
    if(_2month<2):
        _2year-=1
    #print(leap2)
    xdiff = (_1year//400)
    xinit = xdiff*400
    ydiff = (_2year//400)+1
    yinit = ydiff*400
    mount = (((yinit-xinit)//400))*mount
    #print(mount)
    """if mount==0:
        while _1year<=_2year:
            k = _1year%400
            if leap2[k]==1:
                result+=1
            _1year+=1"""
    
    while xinit<_1year:
        m = xinit%400
        if leap2[m]==1:
            count+=1
        xinit+=1
    _2year+=1
    while _2year<=yinit:
        n = _2year%400
        if leap2[n]==1:
            count+=1
        _2year+=1
    result = mount-count
    print(result)
    
    
    
    
    
def check_leapyear(y1):
    if(y1%4==0):
        if(y1%100==0):
            if(y1%400==0):
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0
from collections import defaultdict
import math
import calendar
n = 1
m = 400
leap2 = defaultdict(int)
while n<=m:
        RemindMyDate = calendar.weekday(n,2,7)
        if RemindMyDate==4:
            #count+=1
            leap2[n]+=1
        if RemindMyDate==5:
            leap1 = check_leapyear(n)
            if(leap1==0):
                leap2[n]+=1
                #count+=1
        n+=1
for _ in range(int(input())):
    _1month,_1year = list(map(int,input().split()))
    _2month,_2year = list(map(int,input().split()))
    count=0
    mount = 101
    result = 0
    if(_1month>2):
        _1year+=1
    if(_2month<2):
        _2year-=1
    #print(leap2)
    xdiff = (_1year//400)
    xinit = xdiff*400
    ydiff = (_2year//400)
    yinit = ydiff*400
    kent = ((xdiff+1)*400)
    #mount = (((yinit-xinit)//400))*mount
    #print(mount)
    """if mount==0:
        while _1year<=_2year:
            k = _1year%400
            if leap2[k]==1:
                result+=1
            _1year+=1"""
    
    while xinit<kent:
        m = xinit%400
        if leap2[m]==1:
            count+=1
        xinit+=1
    yinit+=1
    while yinit<=_2year:
        n = _2year%400
        if leap2[n]==1:
            count+=1
        _2year+=1
    result = count + (ydiff-xdiff-1)*mount
    print(result)






def isLeap(year):
    if year%400==0 or year%100!=0 and year%4==0:
        return True
    return False
def day(d, m, y): 
    odd = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4] 
    y -= m < 3
    return (( y + int(y / 4) - int(y / 100) + int(y / 400) + odd[m - 1] + d) % 7)

binYearList=[0]*401
for i in range(1,400):
    d7=day(7,2,i)
    if d7==5:
        binYearList[i]=1
    elif d7==6:
        if not isLeap(i):
            binYearList[i]=1

repeat=sum(binYearList)
for _ in range(int(input())):
    n=len(binYearList)
    m1,y1=map(int,input().split())
    m2,y2=map(int,input().split())
    if m1>2:
        y1+=1
    if m2<2:
        y2-=1
    d1=y1//400
    d2=y2//400
    count=0
    startyr=y1%400
    endyr=y2%400+1
    if d1==d2:
        for i in range(startyr,endyr):
            count+=binYearList[i]
    else:
        for i in range(startyr,401):
            count+=binYearList[i]
        for i in range(endyr):
            count+=binYearList[i]
        count+=(d2-d1-1)*repeat
    print(count)    
    
    
    
    


      

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
    #result = 0
    if(_1month>2):
        _1year+=1
    if(_2month<2):
        _2year-=1
    #print(leap2)
    xdiff = (_1year//400)
    #xinit = xdiff*400
    ydiff = (_2year//400)
    #yinit = ydiff*400
    #kent = ((xdiff+1)*400)
    year1 = _1year%400
    year2 = _2year%400+1
    #mount = (((yinit-xinit)//400))*mount
    #print(mount)
    """if mount==0:
        while _1year<=_2year:
            k = _1year%400
            if leap2[k]==1:
                result+=1
            _1year+=1"""
    
    if xdiff==ydiff:
        for i in range(year1,year2):
            if leap2[i]==1:
                count+=1
    
    else:
        for i in range(year1,401):
            if leap2[i]==1:
                count+=1
        for i in range(year2):
            if leap2[i]==1:
                count+=1
            
        count+=(ydiff-xdiff-1)*mount
    print(count)    
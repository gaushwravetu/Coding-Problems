def expanding(l):
    a = 0
    for i in range(1,len(l)):
        if a>=abs(l[i]-l[i-1]):
            return False
        a = abs(l[i]-l[i-1])
    else:
        return True
def accordian(l):
    if len(l)<3:
        return False
    new = []
    for i in range(len(l)-1):
        k = abs(l[i]-l[i+1])
        new.append(k)
    temp = []
    for j in range(0,len(new)-1):
        if new[j]>new[j+1]:
            temp.append("L")
        if new[j]<new[j+1]:
            temp.append("H")
        if new[j]==new[j+1]:
            temp.append("E")
    if "E" in temp:
        return False
    else:
        for g in range(len(temp)-1):
            if temp[g]==temp[g+1]:
                 return False
        else:
            return True
                        

def max3bad(x,y,z):
  maximum = 0
  if x >= y:
    if x >= z:
      maximum = x
  if y >= z:
    maximum = y
  else:
    maximum = z
  return(maximum)   
        
def max4(w,x,y,z):
  if w >= x and w >= y and w >= z:
    maximum = w
  elif x>=w and x>=y and x>=z:
    maximum = x
  elif y>=w and y>=x and y>=z:
    maximum = y
  else:
    maximum = z
  return(maximum)     

def mypalindrome(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(checkpalindrom(l))
def checkpalindrom(l):
    for i in range(1,len(l)):
        if l[i]==l[(len)-i]:
            return(True)

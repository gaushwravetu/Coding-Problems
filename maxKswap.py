def findMaximumNum(input1, input2, maxm, ctr):
    if input2 == 0:
        return
  
    n = len(input1)
    mx = input1[ctr]
 
    for i in range(ctr+1,n):
        if int(input1[i]) > int(mx):
            mx=input1[i]    
    if(mx!=input1[ctr]):
        input2=input2-1
    for i in range(ctr,n):
        if(input1[i]==mx):
            input1[ctr], input1[i] = input1[i], input1[ctr]
            new_str = "".join(input1)
            if int(new_str) > int(maxm[0]):
                  maxm[0] = new_str
  
            findMaximumNum(input1, input2 , maxm, ctr+1)
            input1[ctr], input1[i] = input1[i], input1[ctr]

def maximiser(cls,input1,input2):
    maxm = [input1]
    result = findMaximumNum(input1, input2, maxm, 0)
    return result

  
if __name__ == "__main__":
    input1 = "129814999"
    input2 = 4
    maxm = [input1]
    input1 = [char for char in input1]
    findMaximumNum(input1, input2, maxm, 0)
    print(maxm[0])
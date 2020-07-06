from itertools import permutations
l1 = permutations('0123')
MySetOfPermutaion = []
for i in list(l1):
   MySetOfPermutaion.append("".join(i))
#print(MySetOfPermutaion)   
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
        p2 = int(MySetOfPermutaion[i][1])
        p3 =int(MySetOfPermutaion[i][2])
        p4 = int(MySetOfPermutaion[i][3])
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
        result1+= l1[0]*25+l1[1]*50+l1[2]*75+l1[3]*100
        if(result1>MaxResult):
            MaxResult = result1
        #print(result1,l1)
    print(MaxResult)
    my_sum+=MaxResult
print(my_sum)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
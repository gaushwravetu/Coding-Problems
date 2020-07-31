for i in range(int(input())):
    matSize = int(input())
    a = 0
    result = []
    for i in range(matSize):
        mat = []
        for j in range(matSize):
            a+=1
            mat.append(a)
        result.append(mat)
    if(matSize%2!=0):
        for i in range(matSize):
            print(*result[i])
    else:
        for i in range(matSize):
            if(i%2==0):
                print(*result[i])
            else:
                print(*list(reversed(result[i])))
            

        
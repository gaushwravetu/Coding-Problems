def sumofFirsts(numbers):
    result = 0
    n = len(numbers)
    for i in range(n):
        if numbers[i]>0:
            flag = False
            temp = numbers[i]
            for x in range(i,n):
                if numbers[x]>=temp:
                    numbers[x]=numbers[x]-temp
                else:
                    break
            result+=temp
        #         elif numbers[x]!=0:
        #             flag=True
        #             result+=i
        #             break
        #     if flag==False:
        #         result+=i
        # print(result)
        # print(numbers)
    return result
n = list(map(int,input().split()))
print(sumofFirsts(n))
    


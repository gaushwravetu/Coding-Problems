def totalArea_quad(quad):
    temp = list()
    totalArea = 0
    position = 0
    #calculation of total area
    while position < len(quad):
        if (not temp) or (quad[temp[-1]] <= quad[position]):
            temp.append(position)
            position += 1
        else:
            top_of_temp = temp.pop()
            area = (quad[top_of_temp] *
                   ((position - temp[-1] - 1)
                   if temp else position))
            totalArea = max(totalArea, area)
    #check condition
    while temp:
        top_of_temp = temp.pop()
        area = (quad[top_of_temp] *
              ((position - temp[-1] - 1)
                if temp else position))
        totalArea = max(totalArea, area)
    return totalArea
#calculation of maximum area to be calculated
def printMax(arr, n, k): 
    max = 0
    i = 0
    while i<(n - k + 1): 
        max = arr[i] 
        for j in range(1, k): 
            if arr[i + j] > max: 
                max = arr[i + j]
        i+=1
        print(str(max) + " ", end = "")

g=int(input())
b,h=map(int,input().split())
varGold=list(map(int,input().split()))

goldArea=totalArea_quad(varGold)

result=((sum(varGold)-goldArea)*b*h)%(10**9+7)
print(result)

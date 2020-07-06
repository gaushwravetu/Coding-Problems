for _ in range(int(input())):
    Coordinates,Query = map(int,input().split())
    CoordinatesList = list(map(int,input().split()))
    for _ in range(Query):
        QueryList = list(map(int,input().split()))
        NoOfIntersection = 0
        for i in range(QueryList[0],QueryList[1]):
            x = ((QueryList[2] - CoordinatesList[i-1])/(CoordinatesList[i]-CoordinatesList[i-1]))+i
            if(x>=i and x<=i+1):
                NoOfIntersection+=1
        print(NoOfIntersection)
            
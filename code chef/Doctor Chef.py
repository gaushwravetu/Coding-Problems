for i in range(int(input())):
    Population, Medicine = map(int,input().split())
    city = list(map(int,input().split()))
    result = 0
    city.sort()
    for i in range(Population):
        if city[i]<=Medicine:
            result+=1
            Medicine = max(Medicine,2*city[i])
        else:
            while(city[i]>Medicine):
                result+=1
                Medicine*=2
            result+=1
            Medicine=2*city[i]
    print(result)

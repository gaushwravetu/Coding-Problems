from collections import defaultdict
for _ in range(int(input())):
    dect1 = defaultdict(int)
    Basket,TypeOfFruit = map(int,input().split())
    typ = list(map(int,input().split()))
    price = list(map(int,input().split()))
    for x in range(Basket):
        dect1[typ[x]]+=price[x]
    print(min(dect1.values()))
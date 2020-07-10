for _  in range(int(input())):
    l = list(map(str,input().split(".")))
    l = '.'.join(l[::-1])
    print(l)
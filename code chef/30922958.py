# cook your dish here
for _ in range(int(input())):
    N,K = map(int,input().split())
    mystr = str(input())
    mylen = len(mystr)
    (uppercase,lowercase) = (0,0)
    for i in mystr:
        if(i.isupper()):
            uppercase+=1
        elif(i.islower()):
            lowercase+=1
    if(uppercase==lowercase):
        if(K>=uppercase):
            print('both')
        else:
            print('none')
    elif(uppercase>lowercase):
        if(K>=uppercase):
            print('both')
        elif(lowercase<K and uppercase>K):
            print('brother')
        elif(K==lowercase):
            print('brother')
        else:
            print('none')
    elif(uppercase<lowercase):
        if(K>=lowercase):
            print('both')
        elif(uppercase<K and lowercase>K):
            print('chef')
        elif(K==uppercase):
            print('chef')
        else:
            print('none')
for i in range(int(input())):
    mystr = str(input())
    strlen = len(mystr)
    i = 0;count=0
    while(i<strlen-1):
        if mystr[i]=='x' and mystr[i+1]=='y' or mystr[i]=='y' and mystr[i+1]=='x':
            count+=1
            i+=2
        else:
            i+=1
    print(count)
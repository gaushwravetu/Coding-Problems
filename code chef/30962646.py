# cook your dish here
for _ in range(int(input())):
    string_list = list(input())
    lenOfString = len(string_list)
    count = 0
    for i in range(0,lenOfString-1):
        if(string_list[i]=='C'):
            if(string_list[i+1]=='E' or string_list[i+1]=='S' or string_list[i+1]=='C'):
                count+=1
            else:
                break
        elif(string_list[i]=='E'):
            if(string_list[i+1]=='S' or string_list[i+1]=='E'):
                count+=1
            else:
                break
        elif(string_list[i]=='S'):
            if(string_list[i+1]=='S'):
                count+=1
            else:
                break
        else:
            break
    #print(count+1)
    if(count+1==lenOfString):
        print('yes')
    else:
        print('no')
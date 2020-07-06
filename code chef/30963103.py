# cook your dish here
for _ in range(int(input())):
    my_number = int(input())
    t = my_number%10
    if(t==0):
        print(0)
    elif(t==5):
        print(1)
    else:
        print(-1)
def compare(a,b):
    if a==b:
        return 'same'
    else:
        return 'different'
for _ in range(int(input())):
    n = int(input())
    if n==1:
        num1 = int(input())
        num2 = int(input())
        print(compare(num1,num2))
    elif n==2:
        str1 = str(input())
        str2 = str(input())
        print(compare(str1,str2))
    elif n==3:
        list1 = list(map(int,input().split()))
        list2 = list(map(int,input().split()))
        print(compare(list1,list2))

    
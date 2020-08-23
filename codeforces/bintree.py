for _ in range(int(input())):
    myinput=input()
    result=''
    if '1' in myinput and '0' in myinput:
        result11=myinput[0]
        if result11=='1':
            result12='0'
        else:
            result12='1'
        for i in range(2*len(myinput)):
            if i%2==0:
                result+=result11
            else:
                result+=result12
    else:
        result=myinput
    print(result)
from collections import deque
for i in range(int(input())):
    mysize = int(input())
    mylist = list(map(int,input().split()))
    mydeque = deque(mylist)
    Right = mydeque.pop()
    Left = mydeque.popleft()
    current = max(Right,Left)
    Flag = False
    while(len(mydeque)>0):
        if Left>=Right and Left<=current:
            current = Left
            Left = mydeque.popleft()
            new = Left
        elif Left<Right and Right<=current:
            current = Right
            Right = mydeque.pop()
            new = Right
        else:
            Flag = True
            break
    if Flag or new>current:
        print('No')
    else:
        print('Yes')

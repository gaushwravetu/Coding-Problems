for _ in range(int(input())):
    NoOfChance = int(input())
    goal = list(input())
    A_NoOfChance = NoOfChance
    B_NoOfChance = NoOfChance
    (A_turn,B_turn) = (0,0)
    ans = 2*NoOfChance
    for i in range(2*NoOfChance):
        if(i%2==0):
            if(goal[i]=='1'):
                A_turn+= int(goal[i])
            A_NoOfChance-=1
        else:
            if(goal[i]=='1'):
                B_turn+= int(goal[i])
            B_NoOfChance-=1
        if(A_turn>B_turn+B_NoOfChance):
            ans = i+1
            break
        else:
            if(B_turn>A_turn+A_NoOfChance):
                ans = i+1
                break
    print(ans)
        
    #print(A_turn,B_turn)
    
    
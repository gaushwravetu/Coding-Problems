def minion_game(string):
    Stuartc=0;Kevinc=0;j=0
    stringlen = len(string)
    voweldict = {'A':1,'E':1,'I':1,'O':1,'U':1}
    for i in string:
        if i in voweldict:
            Kevinc+=stringlen-j
            j+=1
        else:
            Stuartc+=stringlen-j
            j+=1
    if(Kevinc>Stuartc):
        print("{} {}".format('Kevin',Kevinc))
    elif(Kevinc<Stuartc):
        print("{} {}".format('Stuart',Stuartc))
    else:
        print('Draw')


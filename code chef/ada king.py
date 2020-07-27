for i in range(int(input())):
    k = int(input())
    chessBoard = [['X' for a in range (8)] for b in range (8)]
    # print(chessBoard)
    chessBoard[0][0]='O'
    #print(chessBoard)
    if k==1:
        for i in range(8):
            mystr="".join(chessBoard[i])
            print(mystr)
    else:
        for i in range(8):
            for j in range(8):
                if (k-1)==0:
                    break
                if i==0 and j==0:
                    continue
                chessBoard[i][j]='.'
                k-=1
        for i in range(8):
            mystr="".join(chessBoard[i])
            print(mystr)
            
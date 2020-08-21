def PostOrderTraversal(ino, preo, inolen): 
    if preo[0] in ino: 
        root = ino.index(preo[0]) 
          
    if root != 0: 
        PostOrderTraversal(ino[:root],  
                       preo[1:root + 1],  
                       len(ino[:root])) 
      
    if root != inolen - 1:
        PostOrderTraversal(ino[root + 1:],   
                       preo[root + 1:],  
                       len(ino[root + 1:]))
    print(preo[0],end=' ')
          
NoOfNodes = int(input())
inorderlist = list(map(int,input().split()))
preorderlist = list(map(int,input().split()))
inorderlistLen = len(inorderlist)
PostOrderTraversal(inorderlist, preorderlist, inorderlistLen)
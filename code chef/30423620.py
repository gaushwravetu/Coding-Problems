from sys import stdin, stdout
for _ in range(int(stdin.readline())):
    num,query = map(int,stdin.readline().split())
    query_list = list(map(int,stdin.readline().split()))
    query1 = []
    result1 = []
    list1 = []
    list2 = []
    for _ in range(query):
        query1.append(int(stdin.readline()))
        odd = 0
        even = 0
    for i in range(num):
        if(bin(query_list[i]).count('1')%2==0):
            even+=1
        else:
            odd+=1
    for j in range(query):
        if(bin(query1[j]).count('1')%2==0):
            stdout.write(str(even)+" "+str(odd)+"\n")
        else:
            stdout.write(str(odd)+" "+str(even)+"\n")
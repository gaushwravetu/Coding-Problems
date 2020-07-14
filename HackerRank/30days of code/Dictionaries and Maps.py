import sys
testcases = int(sys.stdin.readline().strip())
phonebook = dict()
for i in range(testcases):
    data = sys.stdin.readline().strip().split(' ')
    phonebook[data[0]] = data[1]
checkname = sys.stdin.readline().strip()
while checkname:
    exist = phonebook.get(checkname)
    if exist:
        print("{}={}".format(checkname,exist))
    else:
        print("Not found")
    checkname = sys.stdin.readline().strip()

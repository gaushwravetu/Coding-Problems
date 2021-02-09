from collections import defaultdict
# required_list = [0]*100002
def checkpair(rec_pair):
    if(required_list[rec_pair]==rec_pair):
        return rec_pair
    temp = checkpair(required_list[rec_pair])
    required_list[rec_pair]=temp
    return temp
def merge_pairs(rec_pair1,rec_pair2):
    temp1 = checkpair(rec_pair1)
    temp2 = checkpair(rec_pair2)
    required_list[temp1]=temp2


no_of_volunteers = int(input())
volunteer_list = list(map(int,input().split()))
no_of_pairs = int(input())
mydict = defaultdict(int)
required_list = []
for i in range(no_of_volunteers+1):
    required_list.append(i)
# print(required_list)
for i in range(no_of_pairs):
    pair1,pair2 = map(int,input().split())
    if(checkpair(pair1)!=checkpair(pair2)):
        merge_pairs(pair1,pair2)
max_count = -1
for i in range(no_of_volunteers):
    result = checkpair(i+1)
    mydict[result]+=volunteer_list[i]
    max_count = max(max_count,mydict[result])
print(max_count)




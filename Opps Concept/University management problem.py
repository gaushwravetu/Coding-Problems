class Professor:
    def __init__(self,pid,pname,sdict):
        self.profId = pid
        self.profName = pname
        self.subjectsDict = sdict
class University:
    def getTotalExperience(self, pList, pid):
        for prof in pList:
            if prof.pid==pid:
                return sum(prof.subjectsDict.values())
    def selectSeniorProfessorBySubject(self,plist,subname):
        maxexp = 0
        prevProfId = None
        for prof in plist:
            if subname in prof.subjectsDict.keys():
                if maxexp<prof.subjectsDict[subname]:
                    max = prof.subjectsDict[subname]
                    prevProfId = prof
        return prevProfId
if __name__ == "__main__":
    for _ in range(int(input())):
        plist = []
        pid = int(input())
        pname = input()
        noOfSubjects = int(input())
        sdict = {}
        for i in range(noOfSubjects):
            psub = input()
            pexp = int(input())
            sdict[psub]=pexp
        prof = Professor(pid,pname,sdict)
        plist.append(prof)
        subname = input()
        uni = University()
        inpId = int(input())
        inpName = input()
        print(uni.getTotalExperience(plist,inpId))
        result = uni.selectSeniorProfessorBySubject(plist,inpName)
        if result is None:
            print("No Professor")
        else:
            print(result.profId,result.profName,result.subjectsDict)

        


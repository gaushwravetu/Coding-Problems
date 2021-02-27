class Traveler:
    def __init__(self,tname,tcont,tage,contfrom):
        self.travelerName = tname
        self.traveledCountry = tcont
        self.travelerAge = tage
        self.countryFrom = contfrom
class TravelAgency:
    def __init__(self,tlist):
        self.travelerList = tlist
    def countTravelersTraveledCountry(self,country):
        count = 0
        for i in self.travelerList:
            for j in i.traveledCountry:
                if j==country:
                    count+=1
        return count
    def getTravelerTravelledMaxCountry(self):
        max = 0
        name = ""
        for i in self.travelerList:
            mymax = len(i.traveledCountry)
            if mymax>max:
                max = mymax
                name = i.travelerName
        return name
if __name__ == "__main__":
    n = int(input())
    mylist = []
    for _ in range(n):
        contlist = []
        tname = input()
        tcont = int(input())
        for i in range(tcont):
            tcontname = input()
            contlist.append(tcontname)
        tage = int(input())
        contfrom = input()
        mylist.append(Traveler(tname,contlist,tage,contfrom))
    cont = input()
    obj = TravelAgency(mylist)
    print(obj.countTravelersTraveledCountry(cont))
    print(obj.getTravelerTravelledMaxCountry())

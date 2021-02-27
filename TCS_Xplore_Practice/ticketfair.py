class Passenger:
    def __init__(self,pname,page,distrav):
        self.passengerName = pname
        self.passengerAge = page
        self.distanceTraveled = distrav
    def calculateTicketFare(self,plist,fpkm):
        tax = 0
        tktfare = 0
        for i in plist:
            if i.passengerAge>=60 or i.passengerAge<12:
                tkt = (i.distanceTraveled*fpkm)
                tktfare+=tkt
            elif i.passengerAge>=21 and i.passengerAge<60:
                tkt = i.distanceTraveled*fpkm
                tkt+=tkt*0.12
                tktfare+=tkt
            else:
                tkt = i.distanceTraveled*fpkm
                tkt+=tkt*0.1
                tktfare+=tkt
        return tktfare
    def countSeniorJuniorPassengers(self,plist):
        total = 0
        for i in plist:
            if i.passengerAge>=60 or i.passengerAge<12:
                total+=1
        return total
if __name__ == "__main__":
    n = int(input())
    mylist = []
    for _ in range(n):
        pname = input()
        page = int(input())
        distrav = int(input())
        mylist.append(Passenger(pname,page,distrav))
    ticketfair = int(input())
    obj = Passenger(0,0,0)
    print(obj.calculateTicketFare(mylist,ticketfair))
    print(obj.countSeniorJuniorPassengers(mylist))
        
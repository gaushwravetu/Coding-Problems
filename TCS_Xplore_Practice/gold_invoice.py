class GoldInvoice:
    def __init__(self,iid,ina,iqty,ira,iwei,ipwc,ipdis):
        self.item_id = iid
        self.item_name = ina
        self.item_qty = iqty
        self.item_rate = ira
        self.item_weight = iwei
        self.item_pwc = ipwc
        self.item_pdis = ipdis
    def calc_Item_price_exGST(self,glist,itemchoice):
        item_cost = 0
        for i in glist:
            if(i.item_id==itemchoice):
                itemcost = i.item_qty*i.item_rate*i.item_weight
                pwc = itemcost*(i.item_pwc/100)
                pdis = itemcost*(i.item_pdis/100)
                item_cost+=itemcost+pwc-pdis
        #result = round(item_cost,3)
        return item_cost
    def cal_Item_price_inGST(self,glist,itemchoice):
        item_cost = 0
        for i in glist:
            if(i.item_id==itemchoice):
                itemcost = i.item_qty*i.item_rate*i.item_weight
                pwc = itemcost*(i.item_pwc/100)
                pdis = itemcost*(i.item_pdis/100)
                item_cost+=itemcost+pwc-pdis
        gst = item_cost*0.003
        item_cost+=gst
        return item_cost
if __name__=="__main__":
    n = int(input())
    mylist = []
    for i in range(n):
        iid = int(input())
        iname = input()
        iqty = float(input())
        irate = float(input())
        iweight = float(input())
        ipwc = float(input())
        ipdis = float(input())
        mylist.append(GoldInvoice(iid,iname,iqty,irate,iweight,ipwc,ipdis))
    reqitemid = int(input())
    obj = GoldInvoice(0,"",0,0,0,0,0)
    result1 = obj.cal_Item_price_inGST(mylist,reqitemid)
    result2 = obj.calc_Item_price_exGST(mylist,reqitemid)
    print(round(result1,2))
    print(round(result2,3))


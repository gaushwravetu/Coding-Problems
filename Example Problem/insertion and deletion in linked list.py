class node:
    def __init__(self,v=None):      #defining values and next
        self.value = v
        self.next = None
    def isempty(self):              #checking the condition of empty list
        if self.value == None:
            return(True)
        else:
            return(False)
    def append(self,v):             #formation of linked list
        if self.isempty():
            self.value=v
        elif self.next==None:
            newnode=node(v)
            self.next=newnode

        else:
            self.next.append(v)
            return(v)
    def insert(self,v):             #insertion in linked list
        if self.isempty():
            self.value=v
        return
        newnode = node(v)
        (self.value,newnode.value) = (newnode.value,self.next)
        (self.next,newnode.next) = (newnode,self.next)
        return()
    
    def delete(self,v):         #deletion in linked list
        if self.isempty():
            return
        if self.value == v:
            self.value=None
            if self.next!= None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next!= None:
                self.next.delete(v)
                if self.next.value==None:
                    self.next = None
        return
    def __str__(self):          #printing of linked list
        selflist=[]
        if self.value == None:
            return(str(selflist))
            temp = self
            selflist.append(temp.value)
            while temp.next!=None:
                temp=temp.next
                selflist.append(temp.value)
            return(str(selflist))

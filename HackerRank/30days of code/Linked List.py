
    def insert(self,head,data): 
        newnode = Node(data)
        if not head:
            return newnode
        currentnode = head
        while currentnode.next:
            currentnode = currentnode.next
        currentnode.next = newnode
        return head


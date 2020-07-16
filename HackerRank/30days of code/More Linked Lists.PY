

    def removeDuplicates(self,head):
        if not head:
            return None
        current = head
        while current.next:
            if current.next.data == current.data:
                current.next = current.next.next
            else:
                current = current.next
        return head


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pervious = None
        test = head
        while test:
            res = test.next
            test.next = pervious
            pervious = test
            test = res
        return pervious
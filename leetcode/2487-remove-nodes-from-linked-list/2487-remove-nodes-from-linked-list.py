# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the string
        curr = head
        before = None

        while curr:
            after = curr.next
            curr.next = before
            before = curr
            curr = after
        
        temp = before
        max_ = temp
        temp = temp.next
        while temp:
            if temp.val < max_.val:
                max_.next = temp.next
            else:
                max_.next = temp
                max_ = max_.next
            temp = temp.next
        
        curr = before
        bfr2 = None

        while curr:
            after = curr.next
            curr.next = bfr2
            bfr2 = curr
            curr = after

        return bfr2 
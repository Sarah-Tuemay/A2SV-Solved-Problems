# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        if head:
            even_head = head.next
            even_tail = head.next
        
            while even_tail and even_tail.next:
                if even_tail:
                    odd.next = even_tail.next
                    odd = odd.next
                if odd and even_tail:
                    even_tail.next = odd.next
                    even_tail = even_tail.next
            
            odd.next = even_head

        return head
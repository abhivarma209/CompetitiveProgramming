# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        odd=head
        node=head.next
        even=node
        while odd and even:
            nxt=even.next
            odd.next=nxt
            if nxt:
                odd=nxt
                even.next=nxt.next
                even=nxt.next
            else:
                break
        odd.next=node
        return head
        
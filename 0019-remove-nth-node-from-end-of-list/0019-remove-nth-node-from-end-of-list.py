# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        start,target=head,head
        for _ in range(n):
            start=start.next
        if start == None:
            return head.next
        while start:
            start=start.next
            if start:
                target=target.next
        target.next = target.next.next
        return head
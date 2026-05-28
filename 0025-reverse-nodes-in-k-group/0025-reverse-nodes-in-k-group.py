# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self, head: Optional[ListNode]):
        prev,curr=None,head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev,head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start,node=head,head
        dummy=ListNode(0)
        res=dummy
        while node:
            curr=node
            for _ in range(k-1):
                if curr.next: curr=curr.next
                else: 
                    res.next=node
                    return dummy.next
            nxt=curr.next
            curr.next=None
            start,end = self.rev(node)
            res.next=start
            res=end
            node=nxt
        return dummy.next
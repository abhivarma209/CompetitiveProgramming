# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        curr,prev = head,ListNode(0)
        res=prev
        while curr and curr.next:
            nxt=curr.next
            fast=nxt.next
            nxt.next=curr
            curr.next=fast
            prev.next=nxt
            prev=curr
            curr=fast
            
        return res.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less,greater=ListNode(0),ListNode(0)
        curr=head
        ln,gn=less,greater
        while curr:
            if curr.val<x:
                ln.next=curr
                ln=curr
            else:
                gn.next=curr
                gn=curr
            nxt=curr.next
            curr.next=None
            curr=nxt
        ln.next=greater.next
        return less.next


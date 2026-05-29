# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        node=curr=head
        le=0
        while node:
            node=node.next
            le+=1
        k%=le
        if k==0:
            return head
        for _ in range(k):
            curr=curr.next
        prev=head
        while curr.next:
            curr=curr.next
            prev=prev.next
        res=prev.next
        prev.next=None
        curr.next=head
        return res

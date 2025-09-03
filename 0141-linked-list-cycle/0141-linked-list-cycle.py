# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None or head.next.next == None:
            return False
        slow,fast=head.next,head.next.next
        while slow!=None and fast!=None:
            if slow == fast:
                return True
            slow=slow.next
            if fast.next:
                fast=fast.next.next
            else:
                fast=None
        return False
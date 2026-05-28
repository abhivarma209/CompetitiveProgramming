# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        se=set()
        while head1 or head2:
            if head1:
                if head1 in se:
                    return head1
                se.add(head1)
                head1=head1.next
            if head2:
                if head2 in se:
                    return head2
                se.add(head2)
                head2=head2.next
        return None
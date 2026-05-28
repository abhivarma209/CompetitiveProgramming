# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr and curr.next:
            if curr.next.val==curr.val:
                temp=curr.next
                curr.next=curr.next.next
                temp.next=None
            else:
                curr=curr.next
        return head
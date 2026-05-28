# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr,res=head,dummy
        while curr:
            is_dup=False
            while curr.next:
                if curr.next.val==curr.val:
                    is_dup=True
                    curr=curr.next
                else:
                    break
            print(is_dup,curr.val)
            if not is_dup:
                res.next=curr
                res=curr
            curr=curr.next
        res.next=None
        return dummy.next
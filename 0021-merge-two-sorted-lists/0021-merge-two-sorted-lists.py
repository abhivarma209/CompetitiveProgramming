# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first,second=list1,list2
        res = ListNode(0)
        curr=res
        while first or second:
            if second==None:
                curr.next=first
                curr=first
                first=first.next
                continue
            if first==None:
                curr.next=second
                curr=second
                second=second.next
                continue
            if first.val<second.val:
                curr.next=first
                curr=first
                first=first.next
            else:
                curr.next=second
                curr=second
                second=second.next
        return res.next
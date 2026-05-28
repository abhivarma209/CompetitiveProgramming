# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first,second=l1,l2
        res=ListNode(0)
        curr=res
        carry=0
        while carry or first or second:
            val=(first.val if first else 0)+(second.val if second else 0)+carry
            carry=val//10
            temp=ListNode(val%10)
            curr.next=temp
            curr=temp
            if first: first=first.next
            if second: second=second.next
        return res.next
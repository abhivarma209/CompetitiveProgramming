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
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second = self.rev(slow)
        first = head
        while second:
            if second.val!=first.val:
                return False
            first=first.next
            second=second.next
        return True
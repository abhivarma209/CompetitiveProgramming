class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=nums[0],nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                head=nums[0]
                while head!=slow:
                    slow=nums[slow]
                    head=nums[head]
                return slow
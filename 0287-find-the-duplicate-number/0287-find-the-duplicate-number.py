class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=nums[0],nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        slow1=nums[0]
        while slow1!=slow:
            slow1=nums[slow1]
            slow=nums[slow]
        return slow
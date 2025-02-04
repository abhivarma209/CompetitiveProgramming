class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0] * n

        for i in range(0,n):
            if i == 0:
                res[0]=nums[0]
                continue
            res[i] = nums[i]+res[i-1] if(nums[i]>nums[i-1]) else nums[i]
        
        return max(res)
        
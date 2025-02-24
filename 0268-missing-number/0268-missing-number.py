class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res_nums = [0] * (n+1)
        for num in nums:
            res_nums[num] += 1
        for i,num in enumerate(res_nums):
            if num == 0:
                return i
        return -1
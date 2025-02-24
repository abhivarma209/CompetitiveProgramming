class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tot_sum = n*(n+1)//2
        for num in nums:
            tot_sum -= num
        return tot_sum
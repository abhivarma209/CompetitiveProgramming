class Solution:
    def linear_rob(self, nums):
        if len(nums)==0: return 0
        first,second=0,nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            first,second=second,max(first+nums[i],second)
            res=max(res,second)
        return res
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        return max(self.linear_rob(nums[1:]),self.linear_rob(nums[:-1]))
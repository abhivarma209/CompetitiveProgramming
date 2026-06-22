class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        first,second=0,nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            first,second=second,max(first+nums[i],second)
            res=max(res,second)
        return res
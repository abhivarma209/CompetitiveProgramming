class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr,res=nums[0],nums[0]
        tot=nums[0]
        for i in range(1,len(nums)):
            curr = max(curr+nums[i],nums[i])
            if curr>res:
                res=curr
            tot+=nums[i]
        temp,mi=nums[0],nums[0]
        for i in range(1,len(nums)):
            if temp>0:
                temp=nums[i]
            else:
                if temp+nums[i]>0:
                    temp=nums[i]
                else:
                    temp=temp+nums[i]
            mi =min(mi,temp)
        if tot==mi: return res
        return max(res,tot-mi)
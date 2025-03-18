class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i,j =0,1
        res = 1
        cum_or = nums[0]
        while i<=j and j<len(nums):
            if cum_or&nums[j] == 0:
                res = max(res,j+1-i)
                cum_or |= nums[j]
                j+=1
            else:
                cum_or ^= nums[i]
                i+=1
        return res
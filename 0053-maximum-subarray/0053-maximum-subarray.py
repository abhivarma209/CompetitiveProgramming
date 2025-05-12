class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        n,i=len(nums),0
        while i<n:
            temp = 0
            while i<n and temp>=0:
                temp+=nums[i]
                res=max(res,temp)
                if temp<0:
                    break
                i+=1
            i+=1
        return res
        
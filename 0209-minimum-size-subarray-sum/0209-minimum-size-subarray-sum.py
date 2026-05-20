class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,curr,res=0,0,float('inf')
        for r in range(len(nums)):
            curr+=nums[r]
            while curr>=target:
                res=min(res,r-l+1)
                curr-=nums[l]
                l+=1
        return 0 if res==float('inf') else res
        
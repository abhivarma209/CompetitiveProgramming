class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i,num in enumerate(nums):
            if num>0: break
            if i>0 and nums[i-1]==num:
                continue
            if num>0:
                break
            j,k=i+1,n-1
            while j<k:
                if nums[i]+nums[j]+nums[k] == 0:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j+=1
                else:
                    k-=1
        return list(res)

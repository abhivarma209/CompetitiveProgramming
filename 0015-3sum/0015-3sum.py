class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        se = set()
        for i in range(n):
            if nums[i] > 0: break
            if i>0 and nums[i-1]==nums[i]: continue 
            j,k = i+1,n-1
            while j<k:
                if nums[i]+nums[j]+nums[k] == 0:
                    se.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j+=1
                else:
                    k-=1
        return list(se)
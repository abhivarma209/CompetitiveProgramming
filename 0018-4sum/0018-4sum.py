class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        se = set()
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1,n-2):
                l,r=j+1,n-1
                while l<r:
                    temp = nums[i]+nums[j]+nums[l]+nums[r]
                    if temp == target:
                        se.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                    elif temp<target:
                        l+=1
                    else:
                        r-=1
        return list(se)
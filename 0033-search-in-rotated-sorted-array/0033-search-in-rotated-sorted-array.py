class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if nums[m]>=nums[l]:
                if target<nums[m] and target>=nums[l]:
                    r = m-1
                else:
                    l = m+1
            else:
                if target>nums[m] and target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
        return -1

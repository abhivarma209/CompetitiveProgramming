class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo,hi=0,len(nums)-1
        if nums[lo]==target:
            return True
        while lo<=hi and nums[lo]==nums[hi]:
            lo+=1
        while lo<hi:
            mid=(hi+lo)//2
            if nums[mid]==target:
                return True
            if nums[lo]<=nums[mid]:
                if nums[lo]<=target<nums[mid]:
                    hi=mid-1
                else:
                    lo=mid+1
            else:
                if nums[mid]<target<=nums[hi]:
                    lo=mid+1
                else:
                    hi=mid-1
        if lo<len(nums) and nums[lo]==target:
            return True
        return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        se = set()
        i,j=0,0
        while j-i<=k and j<len(nums):
            if nums[j] in se:
                return True
            se.add(nums[j])
            j+=1
        while j<len(nums):
            se.remove(nums[i])
            i+=1
            if nums[j] in se:
                return True
            se.add(nums[j])
            j+=1
        return False
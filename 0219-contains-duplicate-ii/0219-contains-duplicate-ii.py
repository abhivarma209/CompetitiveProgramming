class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        se = set()
        i,j=0,0
        while j<len(nums):
            if j-i>k:
                se.remove(nums[i])
                i+=1
            se.add(nums[j])
            if len(se)!=j-i+1:
                return True
            j+=1
        return False
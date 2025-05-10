class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        se = set()
        if len(nums)<=k:
            se = set(nums)
            return True if len(se)!=len(nums) else False
        for i in range(k+1):
            se.add(nums[i])
        if len(se)!=k+1:
            return True
        for i in range(k+1,len(nums)):
            se.remove(nums[i-k-1])
            se.add(nums[i])
            if len(se)!=k+1:
                return True
        return False
        
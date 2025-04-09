class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        se = set(nums)
        if min(nums) < k:
            return -1
        return len(se) if k not in se else len(se)-1 
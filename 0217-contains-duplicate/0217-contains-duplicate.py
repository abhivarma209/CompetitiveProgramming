class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        return True if len(nums_set) != len(nums) else False
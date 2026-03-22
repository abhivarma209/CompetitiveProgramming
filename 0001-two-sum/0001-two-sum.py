class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            if seen.get(target-num) != None:
                return [seen.get(target-num),i]
            seen[num]=i
        
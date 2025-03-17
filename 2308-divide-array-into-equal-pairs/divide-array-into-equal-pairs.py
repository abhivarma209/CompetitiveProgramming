class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                s.discard(num)
            else:
                s.add(num)
        return True if len(s) == 0 else False
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if d.get(num) is None:
                d[num] = 1
            else:
                del d[num]
        return True if len(d) == 0 else False
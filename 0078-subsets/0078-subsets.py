class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        res.add(())
        n = len(nums)
        for i in range(n):
            temp = list(res)
            for tup in temp:
                arr = list(tup)
                arr.append(nums[i])
                res.add(tuple(arr))
        result = []
        for tup in list(res):
            result.append(list(tup))
        return result
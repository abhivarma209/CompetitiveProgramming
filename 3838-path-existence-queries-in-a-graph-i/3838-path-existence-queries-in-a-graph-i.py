class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        group = [0] * n
        currentGroup = 0
        for i in range(1,n):
            if nums[i] - nums[i-1] > maxDiff:
                currentGroup += 1
            group[i] = currentGroup
        res = []
        for n1,n2 in queries:
            res.append(group[n1]==group[n2])
        return res
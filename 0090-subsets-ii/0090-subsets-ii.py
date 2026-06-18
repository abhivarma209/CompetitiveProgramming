class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        def dfs(path,idx):
            res.add(tuple(path))
            for i in range(idx,len(nums)):
                path.append(nums[i])
                dfs(path,i+1)
                path.pop()
        dfs([],0)
        return [list(tup) for tup in res]
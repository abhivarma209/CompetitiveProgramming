class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(path,remaining):
            if not remaining:
                res.append(path[:])
                return
            for i,n in enumerate(remaining):
                if i>0 and remaining[i]==remaining[i-1]: continue
                path.append(n)
                dfs(path,remaining[:i]+remaining[i+1:])
                path.pop()
        dfs([],nums)
        return res
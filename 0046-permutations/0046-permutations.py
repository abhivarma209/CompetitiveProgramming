class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(path, remaining):
            if not remaining:
                res.append(path[:])
                return
            for i,n in enumerate(remaining):
                path.append(n)
                dfs(path,remaining[:i]+remaining[i+1:])
                path.pop()
        dfs([],nums)
        return res
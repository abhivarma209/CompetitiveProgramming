class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        di=[[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c]!=1: return
            grid[r][c]=-1
            for dr,dc in di:
                nr,nc=r+dr,c+dc
                if nr<0 or nr>=m or nc<0 or nc>=n or grid[nr][nc]!=1: continue
                if grid[nr][nc]==1:
                    dfs(nr,nc)
        for i in range(m):
            for j in range(n):
                if i in [0,m-1] or j in [0,n-1]:
                    dfs(i,j)
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    res+=1
        return res


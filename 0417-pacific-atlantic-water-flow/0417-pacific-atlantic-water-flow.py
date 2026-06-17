class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(r,c,vis):
            vis.add((r,c))
            for dx,dy in directions:
                nx=r+dx
                ny=c+dy
                if nx<0 or nx>=m or ny<0 or ny>=n or (nx,ny) in vis:
                    continue
                if heights[nx][ny]<heights[r][c]:
                    continue
                dfs(nx,ny,vis)
        pac,atl=set(),set()
        for c in range(n):
            dfs(0,c,pac)
            dfs(m-1,c,atl)
        for r in range(m):
            dfs(r,0,pac)
            dfs(r,n-1,atl)
        return list(pac & atl)
                
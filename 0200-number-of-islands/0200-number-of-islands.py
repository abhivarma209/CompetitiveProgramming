class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis=set()
        m,n=len(grid),len(grid[0])
        di=[[-1,0],[0,-1],[0,1],[1,0]]
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i,j) not in vis:
                    res+=1
                    q=deque([(i,j)])
                    while q:
                        x,y=q.popleft()
                        for dx,dy in di:
                            nx=x+dx
                            ny=y+dy
                            if nx<0 or nx>=m or ny<0 or ny>=n or grid[nx][ny]=='0' or (nx,ny) in vis:
                                continue
                            vis.add((nx,ny))
                            q.append((nx,ny))
        return res
                            
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis=set()
        m,n=len(grid),len(grid[0])
        di=[[-1,0],[0,-1],[0,1],[1,0]]
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in vis:
                    temp=0
                    q=deque([(i,j)])
                    vis.add((i,j))
                    while q:
                        x,y=q.popleft()
                        temp+=1
                        for dx,dy in di:
                            nx=x+dx
                            ny=y+dy
                            if nx<0 or nx>=m or ny<0 or ny>=n or grid[nx][ny]==0 or (nx,ny) in vis:
                                continue
                            vis.add((nx,ny))
                            q.append((nx,ny))
                    res=max(res,temp)
        return res
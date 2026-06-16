class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        vis=set()
        m,n=len(grid),len(grid[0])
        di=[[-1,0],[0,-1],[0,1],[1,0]]
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in vis:
                    q=deque([(i,j)])
                    vis.add((i,j))
                    isBou=False
                    if i==0 or j==0 or i==m-1 or j==n-1:
                        isBou=True
                    count=0
                    while q:
                        x,y=q.popleft()
                        count+=1
                        for dx,dy in di:
                            nx=x+dx
                            ny=y+dy
                            if nx<0 or nx>=m or ny<0 or ny>=n or grid[nx][ny]==0 or (nx,ny) in vis:
                                continue
                            if nx==0 or ny==0 or nx==m-1 or ny==n-1:
                                isBou=True
                            vis.add((nx,ny))
                            q.append((nx,ny))
                    if not isBou:
                        res+=count
        return res
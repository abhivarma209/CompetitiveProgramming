class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque([])
        m=len(grid)
        n=len(grid[0])
        di = [[-1,0],[0,1],[0,-1],[1,0]]
        fr=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                    grid[i][j]=-1
                elif grid[i][j]==1:
                    fr+=1
        if len(q)==0:
            return 0 if fr==0 else -1
        res=0
        while q:
            sz=len(q)
            for _ in range(sz):
                x,y=q.popleft()
                for dx,dy in di:
                    nx=x+dx
                    ny=y+dy
                    if nx<0 or nx>=m or ny<0 or ny>=n or grid[nx][ny]==-1:
                        continue
                    if grid[nx][ny]==1:
                        q.append((nx,ny))
                        grid[nx][ny]=-1
                        fr-=1
            res+=1
        return -1 if fr>0 else res-1
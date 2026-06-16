class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        q=deque([])
        m=len(grid)
        n=len(grid[0])
        di = [[-1,0],[0,1],[0,-1],[1,0]]
        vis=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
                    vis.add((i,j))
        count=1
        while q:
            sz=len(q)
            for _ in range(sz):
                x,y=q.popleft()
                for dx,dy in di:
                    nx=x+dx
                    ny=y+dy
                    if nx<0 or nx>=m or ny<0 or ny>=n or (nx,ny) in vis:
                        continue
                    q.append((nx,ny))
                    vis.add((nx,ny))
                    grid[nx][ny]=count
            count+=1
        return grid
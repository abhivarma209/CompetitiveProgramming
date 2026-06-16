class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        di = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
        q=deque([(0,0,1)])
        n=len(grid)
        visited = set()
        visited.add((0,0))
        res=float('inf')
        while q:
            x,y,l=q.popleft()
            if x==n-1 and y==n-1:
                res=min(res,l)
            for dx,dy in di:
                nx=x+dx
                ny=y+dy
                if nx<0 or nx>=n or ny<0 or ny>=n or grid[nx][ny]==1 or (nx,ny) in visited:
                    continue
                q.append((nx,ny,l+1))
                visited.add((nx,ny))
        return -1 if res==float('inf') else res
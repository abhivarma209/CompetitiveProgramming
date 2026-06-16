class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q=deque([(0,0,0,0)])
        m,n=len(grid),len(grid[0])
        vis={(0,0,0)}
        di =[[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            x,y,blocks,count=q.popleft()
            if x==m-1 and y==n-1: return count
            for dx,dy in di:
                nx=x+dx
                ny=y+dy
                if nx<0 or nx>=m or ny<0 or ny>=n:
                    continue
                nb=blocks+grid[nx][ny]
                if nb>k: continue
                if (nx,ny,nb) in vis: continue
                q.append((nx,ny,nb,count+1))
                vis.add((nx,ny,nb))
        return -1
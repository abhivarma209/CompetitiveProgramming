class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q=deque([])
        m=len(isWater)
        n=len(isWater[0])
        vis = set()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]==1:
                    q.append((i,j,0))
                    vis.add((i,j))
                    isWater[i][j]=0
        di = [[-1,0],[0,-1],[0,1],[1,0]]
        while q:
            sz=len(q)
            for _ in range(sz):
                x,y,l=q.popleft()
                for d in di:
                    nx=x+d[0]
                    ny=y+d[1]
                    if nx<0 or nx>=m or ny<0 or ny>=n or (nx,ny) in vis:
                        continue
                    vis.add((nx,ny))
                    q.append((nx,ny,l+1))
                    isWater[nx][ny]=l+1
        return isWater

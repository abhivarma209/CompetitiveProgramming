class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visit = set()

        def bfs(row,col):
            q = deque()
            q.append((row,col))
            visit.add((row,col))

            while q:
                r,c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dir in directions:
                    nr,nc = r+dir[0],c+dir[1]
                    if nr in range(rows) and nc in range(columns) and grid[nr][nc]=="1" and (nr,nc) not in visit:
                        q.append((nr,nc))
                        visit.add((nr,nc))

        res = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i,j)
                    res+=1

        return res
                        


        
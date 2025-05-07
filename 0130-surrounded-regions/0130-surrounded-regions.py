class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def ifNodeOnEdge(r,c):
            if r==0 or r==rows-1 or c==0 or c==cols-1:
                return True
            return False

        def bfs(r,c)->bool:
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            flag = ifNodeOnEdge(r,c)

            while q:
                row,col=q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    nr,nc = row+dr,col+dc
                    if nr in range(rows) and nc in range(cols) and board[nr][nc]=="O" and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        bfsNodes.add((nr,nc))
                        if ifNodeOnEdge(nr,nc):
                            flag = True

            return flag


        changeNodes = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r,c) not in visited:
                    isEdgeNode = False
                    bfsNodes= set()
                    bfsNodes.add((r,c))
                    isEdgeNode = bfs(r,c)
                    if isEdgeNode == False: changeNodes=changeNodes.union(bfsNodes)

        for nr,nl in changeNodes:
            board[nr][nl] = "X"
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n or board[r][c]!='O':
                return
            board[r][c]='S'
            for dx,dy in directions:
                dfs(r+dx,c+dy)
        
        for r in range(m):
            for c in range(n):
                if (r in [0,m-1] or c in [0,n-1]) and board[r][c]=='O':
                    dfs(r,c)

        for r in range(m):
            for c in range(n):
                if board[r][c]=='O': board[r][c]='X'
                elif board[r][c]=='S': board[r][c]='O'
        
        
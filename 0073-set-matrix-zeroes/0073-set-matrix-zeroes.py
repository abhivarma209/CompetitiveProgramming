class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hs,vs=set(),set()
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    hs.add(i)
                    vs.add(j)
        for num in hs:
            for i in range(n):
                matrix[num][i]=0
        for num in vs:
            for i in range(m):
                matrix[i][num]=0

        
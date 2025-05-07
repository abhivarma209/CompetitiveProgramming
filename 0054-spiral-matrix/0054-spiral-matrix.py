class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        l,t = 0,0
        r,b = n-1,m-1
        i,j=0,0
        res = []
        while t<=b and l<=r:
            if i==t and j==l:
                while j<=r:
                    res.append(matrix[i][j])
                    j+=1
                t+=1
                j-=1
                i=t
            elif i==t and j==r:
                while i<=b:
                    res.append(matrix[i][j])
                    i+=1
                r-=1
                i-=1
                j=r
            elif i==b and j==r:
                while j>=l:
                    res.append(matrix[i][j])
                    j-=1
                b-=1
                j+=1
                i=b
            elif i==b and j==l:
                while i>=t:
                    res.append(matrix[i][j])
                    i-=1
                l+=1
                i+=1
                j=l
        return res
            
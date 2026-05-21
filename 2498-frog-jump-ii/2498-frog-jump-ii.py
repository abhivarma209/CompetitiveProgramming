class Solution:
    def maxJump(self, stones: List[int]) -> int:
        res = stones[1]-stones[0]
        n = len(stones)
        i,j=2,3
        while i<n or j<n:
            if i<n: res = max(res,stones[i]-stones[i-2])
            if j<n: res = max(res,stones[j]-stones[j-2])
            i+=2
            j+=2
        return res

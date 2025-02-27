class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)] 
        arr_map = {val:i for i,val in enumerate(arr)}
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                prev = arr[j] - arr[i]
                check = arr_map.get(prev,-1)
                if check < i and check != -1:
                    dp[i][j] = dp[check][i]+1
                else:
                    dp[i][j] = 2
                if dp[i][j]>2: res = max(res,dp[i][j])
        return res
                

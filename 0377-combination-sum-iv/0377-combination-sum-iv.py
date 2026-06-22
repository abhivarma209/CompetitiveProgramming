class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        for i in range(1,target+1):
            for num in nums:
                if i-num<0:
                    continue
                if i==num:
                    dp[i]+=1
                if not dp[i-num] == 0:
                    dp[i]+=dp[i-num]
        print(dp)
        return 0 if dp[target]==-1 else dp[target]
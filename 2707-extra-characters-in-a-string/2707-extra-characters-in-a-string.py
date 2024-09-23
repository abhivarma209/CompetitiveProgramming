class Solution(object):
    def minExtraChar(self, s, dictionary):
        sz = len(s)
        dp = [sz]*(sz+1)
        se = set(dictionary)
        dp[0]=0
        for i in range(1,sz+1):
            for j in range(i):
                temp=s[j:i]
                if temp in se:
                    dp[i]=min(dp[i],dp[j])
            dp[i]=min(dp[i],dp[i-1]+1)
            
        return dp[sz]
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        
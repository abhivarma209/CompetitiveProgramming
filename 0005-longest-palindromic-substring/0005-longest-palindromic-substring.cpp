class Solution {
public:
    string longestPalindrome(string s) {
       int n=s.length();
        int dp[n][n];
        int maxlen=0,idx=0;
        memset(dp,0,sizeof(dp));
        for(int len = 1;len<=n;len++){
            for(int i = 0,j = len-1;j<n;i++,j++){
                if(len==1) dp[i][j] = 1;
                else if(len==2) dp[i][j] = (s[i]==s[j]);
                else{
                    if(s[i]==s[j] && dp[i+1][j-1]==1) dp[i][j] = 1;
                }
                
                if(dp[i][j]==1){
                    maxlen = len;
                    idx = i;
                }
            }
        }
        return s.substr(idx,maxlen);
    }
};
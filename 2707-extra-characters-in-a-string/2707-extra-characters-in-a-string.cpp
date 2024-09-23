class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        int sz=s.size();
        vector<int>dp(sz+1,sz);
        unordered_set<string>se;
        se.insert(dictionary.begin(),dictionary.end());
        dp[0]=0;
        int res=sz;
        for(int i=1;i<=sz;i++){
            for(int j=0;j<i;j++){
                string temp=s.substr(j,i-j);
                if(se.find(temp)!=se.end()){
                    dp[i]=min(dp[i],dp[j]);
                }
            }
            dp[i]=min(dp[i],dp[i-1]+1);
        }
        return dp[sz];
    }
};
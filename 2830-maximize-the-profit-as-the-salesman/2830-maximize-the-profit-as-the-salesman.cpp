class Solution {
public:
    bool static compare(vector<int>a, vector<int>b){
        return a[1]<b[1];
    }
    int maximizeTheProfit(int n, vector<vector<int>>& offers) {
        vector<int>dp(n,0);
        sort(offers.begin(),offers.end(),compare);
        int mx=0;
        for(int i=0;i<offers.size();i++){
            int temp=0;
            int j=offers[i][0]-1;
            while(j>=0){
                if(dp[j]>0){
                    temp=dp[j];
                    break;
                }
                j--;
            }
            dp[offers[i][1]]=max({dp[offers[i][1]],temp+offers[i][2],mx});
            mx=max(mx,dp[offers[i][1]]);
        }
        int res=0;
        for(int i=0;i<n;i++){
            res=max(res,dp[i]);
        }
        return res;
    }
};
class Solution {
public:
    vector<vector<int>>res;
    void solve(vector<int>&c,int t,int x,int sum,vector<int>&temp){
        if(sum==t){
            res.push_back(temp);
            return;
        }
        if(x>=c.size() || sum>t) return;
        temp.push_back(c[x]);
        solve(c,t,x,sum+c[x],temp);
        temp.pop_back();
        solve(c,t,x+1,sum,temp);
    }
    vector<vector<int>> combinationSum(vector<int>& c, int t) {
        res.clear();
        vector<int>temp;
        solve(c,t,0,0,temp);
        return res;
    }
};
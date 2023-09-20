class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        vector<int>pref;
        unordered_map<int,int>suff;
        pref.push_back(0);
        suff[0]=0;
        int n=nums.size();
        int prefSum=0,suffSum=0;
        for(int i=0;i<n;i++){
            prefSum+=nums[i];
            suffSum+=nums[n-1-i];
            pref.push_back(prefSum);
            suff[suffSum]=i+1;
        }
        int res=INT_MAX;
        for(int i=0;i<=n;i++){
            int pSum=pref[i];
            if(suff.find(x-pSum)!= suff.end()){
                if(i+suff[x-pSum]<=n) res=min(res,i+suff[x-pSum]);
            }
        }
        return res == INT_MAX ? -1: res;
    }
};
class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        unordered_map<int,int>pref;
        unordered_map<int,int>suff;
        pref[0]=0;
        suff[0]=0;
        int n=nums.size();
        int prefSum=0,suffSum=0;
        for(int i=0;i<n;i++){
            prefSum+=nums[i];
            suffSum+=nums[n-1-i];
            pref[prefSum]=i+1;
            suff[suffSum]=i+1;
        }
        int res=INT_MAX;
        for(auto i:pref){
            cout<<i.second<< " ";
            int pSum=i.first;
            if(suff.find(x-pSum)!= suff.end()){
                if(i.second+suff[x-pSum]<=n) res=min(res,i.second+suff[x-pSum]);
            }
        }
        return res == INT_MAX ? -1: res;
    }
};
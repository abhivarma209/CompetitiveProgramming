class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        vector<vector<int>> res;
        for(int i=0;i<n;i++){
            if(nums[i]>0) break;
            if(i>0 && nums[i]==nums[i-1]) continue;
            int l=i+1,r=n-1;
            while(l<r){
                int sum=nums[i]+nums[l]+nums[r];
                if(sum>0) r--;
                else if(sum<0) l++;
                else{
                    res.push_back({nums[i],nums[l],nums[r]});
                    int x=nums[l],y=nums[r];
                    while(l<r && nums[l]==x) l++;
                    while(l<r && nums[r]==y) r--;
                }
            }
        }
        return res;
    }
};